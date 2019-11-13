from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from core.models import Biography, User


class Command(BaseCommand):
    help = 'create users'

    def success(self, message):
        return self.stdout.write(
                self.style.SUCCESS(message)
        )

    def warning(self, warning):
        return self.stdout.write(
                self.style.WARNING(warning)
        )

    def error(self, error):
        return self.stdout.write(
                self.style.ERROR(error)
        )

    def handle(self, *args, **options):
        self.warning(
                'if something goes wrong after fixtres installations,\
                please use: python manage.py flush'
        )

        with transaction.atomic():
            """create user admin"""
            admin = User.objects.create_superuser(
                    email='admin@cotizate.com',
                    password='admin2019'
            )
            Biography.objects.create(
                   terms_cond=True,
                   email_2='admin@cotizate.com',
                   is_complete=True,
                   is_representative=True,
                   user=admin
            )
            self.success('admin user created.')

            """create users creators and contributors"""

            user_creator_1 = User.objects.create_user(
                    name='jhon',
                    last_name='Doe',
                    cellphone='123654',
                    dni='654987',
                    address='here brasil',
                    type_user=1,
                    email='jhondoe@yopmail.com',
                    password='me123',
                    is_active=True
            )
            Biography.objects.create(
                   terms_cond=True,
                   email_2='admin@cotizate.com',
                   is_complete=True,
                   is_representative=True,
                   user=user_creator_1
            )
            user_creator_2 = User.objects.create_user(
                    name='mery',
                    last_name='Doe',
                    cellphone='123654',
                    dni='654987',
                    address='here brasil',
                    type_user=1,
                    email='merydoe@yopmail.com',
                    password='me123',
                    is_active=True
            )
            Biography.objects.create(
                   terms_cond=True,
                   email_2='admin@cotizate.com',
                   is_complete=True,
                   is_representative=True,
                   user=user_creator_2
            )
            self.success('users creators created')

            """user contributors"""
            user_contributor_1 = User.objects.create_user(
                    name='mario',
                    last_name='Lucas',
                    cellphone='123654',
                    dni='654987',
                    address='here other way',
                    type_user=2,
                    email='maricolucas@yopmail.com',
                    password='me123',
                    is_active=True
            )
            Biography.objects.create(
                   terms_cond=True,
                   email_2='mariolucas@cotizate.com',
                   is_complete=True,
                   is_representative=True,
                   user=user_contributor_1
            )
            user_contributor_2 = User.objects.create_user(
                    name='marina',
                    last_name='Lucas',
                    cellphone='123654',
                    dni='654987',
                    address='here beyond away',
                    type_user=2,
                    email='marinalucas@yopmail.com',
                    password='me123',
                    is_active=True
            )
            Biography.objects.create(
                   terms_cond=True,
                   email_2='marinalucas@cotizate.com',
                   is_complete=True,
                   is_representative=True,
                   user=user_contributor_2
            )
            self.success('user contributors created.')
