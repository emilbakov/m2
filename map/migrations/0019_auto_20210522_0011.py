# Generated by Django 3.0.8 on 2021-05-21 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_auto_20210522_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huntingspot',
            name='animals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='map.Animal'),
        ),
    ]