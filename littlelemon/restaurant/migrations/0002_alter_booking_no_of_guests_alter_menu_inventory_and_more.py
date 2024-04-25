# Generated by Django 5.0.4 on 2024-04-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
