# Generated by Django 4.0.2 on 2022-04-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_reserved_seat_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
