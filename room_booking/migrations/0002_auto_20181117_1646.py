# Generated by Django 2.1.2 on 2018-11-17 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='facilites',
            new_name='facilities',
        ),
    ]