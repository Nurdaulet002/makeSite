# Generated by Django 3.1 on 2020-11-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_clothes', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='select',
            field=models.CharField(choices=[('1 star', '1 Star'), ('2 satr', '2 Star'), ('3 star', '3 Star'), ('4 star', '4 Star'), ('5 star', '5 Star')], default='5 star', max_length=50, null=True),
        ),
    ]
