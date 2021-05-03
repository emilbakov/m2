# Generated by Django 3.0.8 on 2020-07-15 08:03

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20200715_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huntingspot',
            name='geom2',
        ),
        migrations.AddField(
            model_name='huntingspot',
            name='address',
            field=djgeojson.fields.PointField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='huntingspot',
            name='geom',
            field=djgeojson.fields.PolygonField(),
        ),
    ]