from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
        PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """create and saves a new user"""
        if not email:
            raise ValueError('users must have a email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    USER_TYPE = (
            (1, 'create user'),
            (2, 'contributor user'),
    )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='')
    cellphone = models.CharField(max_length=255, default='')
    dni = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=300, default='')
    photo = models.CharField(max_length=250, blank=True)
    type_user = models.IntegerField(choices=USER_TYPE, default=1)
    created_at = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class CodeActivation(models.Model):
    code_token = models.CharField(max_length=255, blank=True)
    is_expired = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_token


class Biography(models.Model):
    terms_cond = models.BooleanField(default=True)
    updated_at = models.DateTimeField(blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    email_2 = models.CharField(max_length=255, blank=True)
    b_facebook = models.CharField(max_length=255, blank=True)
    b_twitter = models.CharField(max_length=255, blank=True)
    b_linkedin = models.CharField(max_length=255, blank=True)
    b_instagram = models.CharField(max_length=255, blank=True)
    is_complete = models.BooleanField(default=False)
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.user.name + '  ' + self.user.last_name
