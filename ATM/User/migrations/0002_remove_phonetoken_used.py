# Generated by Django 4.2.3 on 2023-09-15 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_phone_login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonetoken',
            name='used',
        ),
    ]
