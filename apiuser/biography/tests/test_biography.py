from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Biography
from biography.serializers import BiographySerializer


BIOGRAPHY_URL = reverse('biography')


class BiographyUserTests(TestCase):
    """test user Biography updated"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """test login is required for update data user"""
        res = self.client.get(BIOGRAPHY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateBiographyTests(TestCase):
    """test the authorized user biography API"""

    def setUp(self):
        self.user = get_user_model().objects.get(id=2)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_biography(self):
        """test retrieving tags"""
        Biography.objects.create(user=self.user,
                terms_cond=True,
                updated_at=timezone.now(),
                address_2='',
                email_2='',
                b_facebook='https://facebook.com/me',
                b_twitter='',
                b_linkedin='',
                b_instagram='',
                is_complete=True
        )
        Biography.objects.create(user=self.user,
                terms_cond=True,
                updated_at=timezone.now(),
                address_2='anywhere and why',
                email_2='me@sendonemail.com',
                b_facebook='https://facebook.com/me',
                b_twitter='',
                b_linkedin='',
                b_instagram='',
                is_complete=True
        )
        res = self.client.get(BIOGRAPHY_URL)
        biography = Biography.objects.all().order_by('-name')
        serializer = BiographySerializer(biography, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_biography_successful(self):
        """test creating a new biography user"""

        payload = {'id':self.user,
                'terms_cond':True,
                'updated_at':timezone.now(),
                'address_2':'anywhere and why',
                'email_2':'me@sendonemail.com',
                'b_facebook':'https://facebook.com/me',
                'b_twitter':'',
                'b_linkedin':'',
                'b_instagram':'',
                'is_complete':True
        }
        res = self.client.post(BIOGRAPHY_URL, payload)
        self.assertTrue(res.is_complete)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


