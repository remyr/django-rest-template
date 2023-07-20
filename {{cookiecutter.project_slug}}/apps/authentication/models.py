from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import NanoIDField

class User(AbstractUser):
    id = NanoIDField(primary_key=True)
    subclaim = models.CharField(max_length=255, unique=True, blank=True, null=True)
