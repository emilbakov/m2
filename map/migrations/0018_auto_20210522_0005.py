# Generated by Django 3.0.8 on 2021-05-21 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0017_auto_20210521_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huntingspot',
            name='animals',
        ),
        migrations.AddField(
            model_name='huntingspot',
            name='animals',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='map.Animal'),
            preserve_default=False,
        ),
    ]
