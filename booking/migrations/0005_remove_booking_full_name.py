# Generated by Django 5.1.4 on 2024-12-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='full_name',
        ),
    ]