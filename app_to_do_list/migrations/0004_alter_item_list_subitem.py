# Generated by Django 4.1.1 on 2022-09-13 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_do_list', '0003_rename_owning_list_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='app_to_do_list.list'),
        ),
        migrations.CreateModel(
            name='Subitem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_to_do_list.item')),
                ('parent_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_subitems', to='app_to_do_list.item')),
            ],
            bases=('app_to_do_list.item',),
        ),
    ]