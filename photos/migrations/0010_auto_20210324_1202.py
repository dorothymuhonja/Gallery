# Generated by Django 3.1.7 on 2021-03-24 09:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20210324_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='images'),
        ),
    ]