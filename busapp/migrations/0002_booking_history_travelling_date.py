# Generated by Django 5.1.4 on 2025-03-12 12:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_history',
            name='travelling_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
