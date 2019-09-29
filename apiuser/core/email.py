from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class CotizateSendEmail(EmailMultiAlternatives):
    """this is a class is a wrappter that allow
    us to create may type of email, to send this,
    just instantiate and set the HTML path for the
    email, this allow us to customize email sending
    without too much effort.
    To use custom templates please use this as example:
    send_email_with_custom_template(
        template_name='email/activation/activation.html',
        context={
            'username': 'jhon',
            'email': 'jhon@ngelrojasp.com'}
            .....)
    *OBS: you can choose pass the context or not.
    *OBS: this should always be used as a task from celery."""

    def __init__(
            self, subject='', body='', from_email=None, to=None, bcc=None,
            connection=None, attachments=None, headers=None, cc=None,
            reply_to=None,):
        """initialize parent class with the default attrs"""
        super().__init__(
                subject, body, from_email, to, bcc,
                connection, attachments, headers, cc,
                reply_to,
        )

    def send_email_with_custom_template(
            self, template_name: str, context: dict,):
        email_html_message = render_to_string(template_name, context)
        self.attach_alternative(email_html_message, 'text/html')
        self.send(fail_silently=False)
        return self
