# Generated by Django 4.0.2 on 2022-05-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0006_transection_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='isHouseFull',
            field=models.BooleanField(default=False),
        ),
    ]