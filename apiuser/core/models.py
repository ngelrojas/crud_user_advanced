from django.utils.timezone import now
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
    created_at = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        full_name = '%s %s' % (self.name, self.last_name)
        return full_name.strip()


class CodeActivation(models.Model):
    code_token = models.CharField(max_length=255, blank=True)
    is_expired = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_token


class Biography(models.Model):
    terms_cond = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    email_2 = models.CharField(max_length=255, blank=True)
    b_facebook = models.CharField(max_length=255, blank=True)
    b_twitter = models.CharField(max_length=255, blank=True)
    b_linkedin = models.CharField(max_length=255, blank=True)
    b_instagram = models.CharField(max_length=255, blank=True)
    is_complete = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)
    personal_website = models.CharField(max_length=255, blank=True)
    company_website = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    company_nit = models.CharField(max_length=255, blank=True)
    company_city = models.CharField(max_length=255, blank=True)
    company_phone = models.CharField(max_length=255, blank=True)
    company_address = models.CharField(max_length=300, blank=True)
    company_email = models.CharField(max_length=255, blank=True)
    company_logo = models.CharField(max_length=255, blank=True)
    company_description = models.CharField(max_length=255, blank=True)
    company_facebook = models.CharField(max_length=255, blank=True)
    company_twitter = models.CharField(max_length=255, blank=True)
    company_linkedin = models.CharField(max_length=255, blank=True)
    company_instagram = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.get_full_name()


class Campaing(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category_id = models.IntegerField()
    tag_id = models.IntegerField()
    reward_id = models.IntegerField()
    budget = models.FloatField(null=True, blank=True)
    qty_days = models.IntegerField()
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    video = models.CharField(max_length=255, blank=True)
    excerpt = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    public_at = models.DateTimeField(null=True, blank=True)
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title + '  ' + self.user.get_full_name()


class TagCampaing(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class CategoryCampaing(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Reward(models.Model):

    REWARD_TYPE = (
            (1, 'donation'),
            (2, 'contribution')
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    type_reward = models.IntegerField(choices=REWARD_TYPE, default=1)
    delivery_data = models.DateTimeField()
    delivery_place = models.CharField(max_length=400, blank=True)
    description = models.CharField(max_length=800, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=now)
    user_reward = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.name + '  ' + self.user.last_name
