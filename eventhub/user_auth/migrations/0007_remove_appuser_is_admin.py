# Generated by Django 4.0.3 on 2022-04-11 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_alter_appuser_first_name_alter_appuser_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='is_admin',
        ),
    ]
