# Generated by Django 4.0.3 on 2022-04-15 10:52

import django.core.validators
from django.db import migrations, models
import eventhub.categories.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='brief_description',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(100), eventhub.categories.validators.only_letters_and_space_validator]),
        ),
        migrations.AlterField(
            model_name='event',
            name='topic',
            field=models.CharField(max_length=35, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(35), eventhub.categories.validators.only_letters_and_space_validator]),
        ),
    ]
