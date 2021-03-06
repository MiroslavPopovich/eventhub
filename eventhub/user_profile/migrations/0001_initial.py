# Generated by Django 4.0.3 on 2022-04-11 08:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import eventhub.user_profile.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), eventhub.user_profile.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), eventhub.user_profile.validators.only_letters_validator])),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[eventhub.user_profile.validators.MaxFileSizeInMbValidator(2)])),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
