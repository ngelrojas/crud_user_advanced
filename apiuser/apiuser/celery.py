from __future__ import absolute_import
from __future__ import unicode_literals

import os
from decimal import Decimal
import requests
from celery import Celery
from celery import shared_task
from django.conf import settings
from core.email import CotizateSendEmail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiuser.settings')
app = Celery('apiuser', broker='pyamqp://guest@localhost//')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@shared_task(bind=True)
def send_email_message(
        self, subject, to, body, template_name=None, context=None
    ):
    try:
        CotizateSendEmail(
                subject=subject,
                to=to,
                from_email=settings.DEFAULT_FROM_EMAIL,
                body=body,
        ).send_email_with_custom_template(
                template_name=template_name,
                context=context,
        )
        return True
    except Exception as e:
        return self.retry(exc=e, countdown=10)
