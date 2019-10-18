from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """test creating user with valid payload is successful"""
        payload = {
                'email': 'me@ngelrojasp.com',
                'password': 'me123',
                'name': 'test name',
                'last_name': 'test last name',
                'dni': '987564',
                'cellphone': '123654',
                'address': 'for here'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # user = get_user_model().objects.get(**res.data)
        # self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """test creating user that already exists fails"""
        payload = {'email': 'me@ngelroajsp.com', 'password': 'me123'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """test that the password must be more than 5 characters"""
        payload = {'email': 'me@ngelrojasp.com', 'password': 'me'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
                email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """test that a token is created for the user"""
        payload = {'email': 'me@ngelrojasp.com',
                   'password': 'me123',
                   'is_active': True}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """test that token is not create if invalid credentials are given"""
        create_user(email='me@ngelrojasp.com', password='me123')
        payload = {'email': 'me@ngelroasp.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """test that token is not created if user dont exists"""
        payload = {'email': 'me@ngelroajsp.com', 'password': 'me123'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """test that email and passwrod are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': '1'})
        self.assertNotIn('tokekn', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """test that authentication is required for users"""
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """test api requests that require authentication"""

    def setUp(self):
        self.user = create_user(
                email='me@ngelrojasp.com',
                password='me123',
                name='ngel',
                last_name='rojas',
                dni='123654',
                cellphone='654987',
                address='for there'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """test retrieving profile for logged in used"""
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertEqual(res.data, self.user)

    def test_post_me_not_allowed(self):
        """test that post is not allowed on the me url"""
        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """test updating the user profile for authenticated user"""
        payload = {'name': 'new name', 'password': 'me123'}
        res = self.client.patch(ME_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
