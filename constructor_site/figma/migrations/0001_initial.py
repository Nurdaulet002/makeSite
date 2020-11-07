# Generated by Django 3.1.2 on 2020-11-07 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('top', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(default='Описание', max_length=30)),
                ('detail', models.TextField(default='Подробности', max_length=30)),
                ('Shipping_Returns', models.TextField(default='Доставка и Возврат', max_length=30)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='figma.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
