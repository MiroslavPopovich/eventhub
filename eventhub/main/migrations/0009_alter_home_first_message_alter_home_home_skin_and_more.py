# Generated by Django 4.0.3 on 2022-04-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_home_topic_first_message_home_topic_second_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='first_message',
            field=models.TextField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='home',
            name='home_skin',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='home',
            name='second_message',
            field=models.TextField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='home',
            name='third_message',
            field=models.TextField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='home',
            name='topic_first_message',
            field=models.CharField(default='', max_length=26),
        ),
        migrations.AlterField(
            model_name='home',
            name='topic_second_message',
            field=models.CharField(default='', max_length=26),
        ),
        migrations.AlterField(
            model_name='home',
            name='topic_third_message',
            field=models.CharField(default='', max_length=26),
        ),
        migrations.AlterField(
            model_name='home',
            name='topic_welcome_message',
            field=models.CharField(default='', max_length=26),
        ),
        migrations.AlterField(
            model_name='home',
            name='welcome_message',
            field=models.TextField(default='', max_length=256),
        ),
    ]