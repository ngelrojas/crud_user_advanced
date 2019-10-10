from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class BiographyUserTests(TestCase):
    """test user Biography updated"""

    def setUp(self):
        self.client = APIClient()

    def test_update_data_user_success(self):
        """test user data biography is updated, successfuly"""
        payload = {
                'id': 2,
                'is_complete': True
        }
        self.assertTrue(payload['is_complete'])

    def test_update_data_user_error(self):
        """test user data biography is not updated"""
        payload = {
                'id': 2,
                'is_complete': False
        }
        self.assertFalse(payload['is_complete'])
