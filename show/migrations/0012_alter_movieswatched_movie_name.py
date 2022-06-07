# Generated by Django 4.0.2 on 2022-06-07 07:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0011_remove_movieswatched_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieswatched',
            name='movie_name',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False),
        ),
    ]
