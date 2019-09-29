from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,\
        urlsasfe_base64_decode
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from core.tokens import account_activation_token


CREATE_USER_URL = reverse('user:create')


class SendEmailUserTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_send_email_successful(self):
        """test send email successfuly"""
        payload = {
                'email': 'jhon@gmail.com',
                'password': 'me123',
                'name': 'jhon doe'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_send_email_notsend(self):
        """test not send email"""
        payload = {
                'email': 'jhon@gmail.com',
                'password': 'me123',
                'name': 'jhon doe'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_creating_code_confirmation(self):
        """test creating code activation user"""
        payload = {
                'email': 'jhon@gmail.com',
                'password': 'me123',
                'name': 'jhon doe'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        user = get_user_model().objects.get(**res.data)

        uuid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

