import datetime
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        """creating a value to current user"""
        now = datetime.datetime.now().minute
        user_now = six.text_type(user.pk) + six.text_type(now)
        hashed_string = user_now + six.text_type(user.is_active)
        return hashed_string

    def make_token(self, user):
        """
        Returns a token that can be used once to do a password reset
        for the given user.
        """
        now = self._num_days(self._today())
        token_generated = self._make_token_with_timestamp(user, now)
        return token_generated


def encode_user_id(id):
    return urlsafe_base64_encode(force_bytes(id))


def decode_user_id(id):
    return force_text(urlsafe_base64_decode(id))


def make_user_token(user):
    generator = TokenGenerator()
    return generator.make_token(user)
