# Generated by Django 3.0.8 on 2021-05-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0019_auto_20210522_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huntingspot',
            name='animals',
        ),
        migrations.AddField(
            model_name='animal',
            name='huntingspot',
            field=models.ManyToManyField(to='map.HuntingSpot'),
        ),
    ]