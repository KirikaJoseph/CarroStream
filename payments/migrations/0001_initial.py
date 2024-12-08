# Generated by Django 5.1.4 on 2024-12-06 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.booking')),
                ('method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.paymentmethod')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='invoices/')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.payment')),
            ],
        ),
    ]
