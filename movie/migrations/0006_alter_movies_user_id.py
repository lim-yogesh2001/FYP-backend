# Generated by Django 4.0.2 on 2022-04-16 17:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0005_movies_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='user_id',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
