# Generated by Django 5.1.4 on 2024-12-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
