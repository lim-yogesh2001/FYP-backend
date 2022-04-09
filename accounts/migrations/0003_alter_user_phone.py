# Generated by Django 4.0.2 on 2022-04-09 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_groups_alter_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please Enter the number in 9999999999 format.', regex='^\\??\\d{9,10}$')]),
        ),
    ]
