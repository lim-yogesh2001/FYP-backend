# Generated by Django 4.0.2 on 2022-04-09 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0002_alter_seats_options_alter_shows_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved_seat',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
