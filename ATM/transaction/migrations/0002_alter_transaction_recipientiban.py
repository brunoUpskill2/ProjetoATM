# Generated by Django 4.2.5 on 2023-11-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='recipientIBAN',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
