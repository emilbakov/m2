# Generated by Django 3.0.8 on 2021-05-08 15:30

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HuntingSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('geom', djgeojson.fields.GeometryCollectionField()),
                ('hardurl', models.CharField(blank=True, max_length=256, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
