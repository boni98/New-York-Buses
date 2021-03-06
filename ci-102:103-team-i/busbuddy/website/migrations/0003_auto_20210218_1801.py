# Generated by Django 3.1.6 on 2021-02-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=100)),
                ('currentLocation', models.CharField(default='', max_length=200)),
                ('closestBusStop', models.CharField(default='', max_length=200)),
                ('route', models.CharField(default='', max_length=200)),
                ('ETA', models.CharField(default='', max_length=100)),
                ('ride_date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='closestBusStop',
            new_name='destination',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='ETA',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='currentLocation',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='ride_date',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='route',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='user_id',
        ),
    ]
