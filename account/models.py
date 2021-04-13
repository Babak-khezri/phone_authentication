from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .managers import PhoneUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, unique=True)
    otp = models.PositiveBigIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'

    objects = PhoneUserManager()
    REQUIRED_FIELDS = []
    # backends = ''
