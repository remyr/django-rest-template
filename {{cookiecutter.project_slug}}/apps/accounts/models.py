from functools import partial
from nanoid import generate
from charidfield import CharIDField
from django.contrib.auth.models import AbstractUser


def generate_nanoid():
    return generate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


NanoIDField = partial(
    CharIDField,
    default=generate_nanoid,
    max_length=30,
    help_text="nanoid-format identifier for this entity."
)


class User(AbstractUser):
    id = NanoIDField(primary_key=True)
