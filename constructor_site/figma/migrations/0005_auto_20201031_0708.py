# Generated by Django 3.1.2 on 2020-10-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figma', '0004_good_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(default='DEFAULT', max_length=30),
        ),
        migrations.AddField(
            model_name='good',
            name='detail',
            field=models.TextField(default='DEFAULT VALUE', max_length=30),
        ),
    ]
