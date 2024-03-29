# Generated by Django 3.1 on 2020-11-07 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_site', '0001_initial'),
        ('sale_clothes', '0008_remove_comment_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_site.usersite'),
        ),
        migrations.AddField(
            model_name='good',
            name='user_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_site.usersite'),
        ),
        migrations.AddField(
            model_name='undercategory',
            name='user_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_site.usersite'),
        ),
    ]
