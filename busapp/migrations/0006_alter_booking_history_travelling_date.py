# Generated by Django 5.1.4 on 2025-03-12 13:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0005_alter_booking_history_travelling_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_history',
            name='travelling_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
