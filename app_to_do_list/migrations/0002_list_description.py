# Generated by Django 4.1.1 on 2022-09-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='description',
            field=models.TextField(default='this is a description of your task'),
            preserve_default=False,
        ),
    ]
