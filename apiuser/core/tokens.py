from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_has_value(self, user, timestamp):
        """creating a value to current user"""
        return(
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_activate)
        )

account_activation_token = TokenGenerator
