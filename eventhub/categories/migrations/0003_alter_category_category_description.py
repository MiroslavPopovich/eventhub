# Generated by Django 4.0.3 on 2022-04-15 10:52

import django.core.validators
from django.db import migrations, models
import eventhub.categories.validators


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(35), eventhub.categories.validators.only_letters_and_space_validator]),
        ),
    ]
