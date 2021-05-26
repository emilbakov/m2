# Generated by Django 3.0.8 on 2021-05-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0021_auto_20210522_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sleep',
            name='huntingspot',
        ),
        migrations.AddField(
            model_name='huntingspot',
            name='sleeps',
            field=models.ManyToManyField(to='map.Sleep'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5),
        ),
    ]