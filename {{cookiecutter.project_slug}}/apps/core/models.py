from functools import partial
from nanoid import generate
from charidfield import CharIDField
from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_nanoid():
    return generate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


NanoIDField = partial(
    CharIDField,
    default=generate_nanoid,
    max_length=30,
    help_text="nanoid-format identifier for this entity."
)

class BaseModel(models.Model):
    id = NanoIDField(primary_key=True)
    class Meta:
        abstract = True

class TimeStampedModel(BaseModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True