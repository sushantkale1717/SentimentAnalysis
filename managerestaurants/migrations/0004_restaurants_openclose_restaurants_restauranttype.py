# Generated by Django 4.1.4 on 2023-01-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerestaurants', '0003_restaurants_rimg_restaurants_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='openclose',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='restaurantType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
