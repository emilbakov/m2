# Generated by Django 3.0.8 on 2021-05-10 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_sleep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sleep',
            old_name='realtors',
            new_name='huntingspot',
        ),
    ]