# Generated by Django 4.1.1 on 2022-09-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_do_list', '0006_remove_list_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='description',
            field=models.TextField(default='-'),
        ),
    ]