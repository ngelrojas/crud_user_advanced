from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import TagCampaing

from tag.serializers import TagCampaingSerializer


class PublicTagCampaingTests(TestCase):
    """test the public available tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """test that login is required for retrieven tags"""
        res = self.client.get('/api/v1/tag')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagCamapingTests(TestCase):
    """test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_tags(self):
        """test retrieving tags"""
        TagCampaing.objects.create(name='fist tag')
        TagCampaing.objects.create(name='second tag')
        res = self.client.get('/api/v1/tag')
        tags = TagCampaing.objects.all().order_by('-name')
        serializer = TagCampaingSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """test that tags returned are for the authenticated user"""
        TagCampaing.objects.create(name='thrid tag')
        tag = TagCampaing.objects.create(name='fourth tag')
        res = self.client.get('/api/v1/tag')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
