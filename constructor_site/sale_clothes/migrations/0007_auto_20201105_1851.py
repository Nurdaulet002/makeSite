# Generated by Django 3.1 on 2020-11-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_clothes', '0006_auto_20201105_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='select',
            field=models.BooleanField(default=False),
        ),
    ]
