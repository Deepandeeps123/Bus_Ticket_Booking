# Generated by Django 5.1.4 on 2025-03-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0003_alter_booking_history_ticket_no_alter_bus_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.IntegerField(),
        ),
    ]
