# Generated by Django 3.0.8 on 2021-05-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20210503_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='huntingspot',
            old_name='url',
            new_name='hardurl',
        ),
    ]
