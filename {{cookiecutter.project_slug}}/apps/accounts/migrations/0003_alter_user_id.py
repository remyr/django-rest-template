# Generated by Django 4.1.3 on 2022-11-02 20:09

import charidfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=charidfield.fields.CharIDField(
                default="SXaQkI7J5lud1oZiT8C8H",
                help_text="nanoid-format identifier for this entity.",
                max_length=30,
                prefix="",
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
