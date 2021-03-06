# Generated by Django 4.0.3 on 2022-04-15 09:20

import django.core.validators
from django.db import migrations, models
import eventhub.user_profile.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_remove_appuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), eventhub.user_profile.validators.only_letters_validator]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), eventhub.user_profile.validators.only_letters_validator]),
        ),
    ]
