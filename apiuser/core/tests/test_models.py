from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(self, email='me@ngelrojasp.com', password='me123'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'me@ngelrojasp.com'
        password = 'me123'
        user = get_user_model().objects.create_user(
                    email=email,
                    password=password
                )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """test the email for a new user is normalized"""
        email = 'me@NGELROJASP.com'
        user = get_user_model().objects.create_user(email, 'me123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'me123')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
                'admin@ngelrojasp.com',
                'admin123'
                )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

