# Generated by Django 4.0.2 on 2022-04-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='casts',
            field=models.CharField(default='Not Defined', max_length=100),
        ),
    ]
