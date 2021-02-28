from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=150, blank=True)
