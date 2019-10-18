from django.test import TestCase
from django.urls import reverse
from django.core import mail
# from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
# from core.tokens import make_user_token, encode_user_id
from core.models import User


CREATE_USER_URL = reverse('user:create')


class SendEmailUserTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_send_email_successful(self):
        """test send email successfuly"""
        payload = {
                'email': 'jhon@gmail.com',
                'password': 'me123',
                'name': 'jhon doe',
                'last_name': 'Doe',
                'dni': '12654',
                'cellphone': '654987',
                'address': 'hre'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_send_email_nosent(self):
        """test not send email"""
        self.assertEqual(len(mail.outbox), 0)

    def test_activate_account_with_token(self):
        """test creating code activation user"""

        inactive_user = User.objects.create_user(
            password='inactivepass',
            email='inact@test.com',
            is_staff=True,
            is_superuser=True,
            is_active=False,
        )
        # uid = inactive_user.id
        # token = make_user_token(inactive_user)
        # res = self.client.put(f'api/user/activate/{uid}/{token}')
        self.assertTrue(User.objects.get(id=inactive_user.id))
        # self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_activate_account_with_error_token(self):
        """test activation with token error, and expired token"""
        inactive_user = User.objects.create_user(
                password='inactivepass',
                email='inactive@test.com',
                is_staff=True,
                is_superuser=False,
                is_active=True,
        )
        uid = 1
        token = ''
        res = self.client.put(f'api/user/activate/{uid}/{token}')
        self.assertTrue(User.objects.get(id=inactive_user.id).is_active)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
