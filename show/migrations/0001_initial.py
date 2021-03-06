# Generated by Django 4.0.2 on 2022-06-08 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theater', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesWatched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='images/movies_watched')),
                ('show_id', models.CharField(blank=True, max_length=10)),
                ('show_time', models.TimeField()),
                ('date', models.DateField()),
                ('theater_name', models.CharField(blank=True, max_length=100)),
                ('row', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved_Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.TimeField()),
                ('date', models.DateField()),
                ('langauge', models.CharField(max_length=100)),
                ('isHouseFull', models.BooleanField(default=False)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movies')),
                ('theater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.theaters')),
            ],
            options={
                'verbose_name_plural': 'Shows',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.shows')),
            ],
            options={
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='Transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transection_code', models.CharField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('reserved_seat_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='show.reserved_seat')),
                ('ticket_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='show.tickets')),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('theater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.theaters')),
            ],
            options={
                'verbose_name_plural': 'Seats',
            },
        ),
        migrations.AddField(
            model_name='reserved_seat',
            name='seat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.seats'),
        ),
        migrations.AddField(
            model_name='reserved_seat',
            name='show_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.shows'),
        ),
        migrations.AddField(
            model_name='reserved_seat',
            name='ticket_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='show.tickets'),
        ),
        migrations.AddField(
            model_name='reserved_seat',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
