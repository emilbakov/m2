# Generated by Django 3.0.8 on 2021-05-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0020_auto_20210522_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='huntingspot',
        ),
        migrations.AddField(
            model_name='huntingspot',
            name='animals',
            field=models.ManyToManyField(to='map.Animal'),
        ),
    ]
