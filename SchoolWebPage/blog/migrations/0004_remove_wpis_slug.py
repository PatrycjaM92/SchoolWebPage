# Generated by Django 4.1 on 2022-08-06 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_data_utowrzenia_wpis_data_utworzenia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpis',
            name='slug',
        ),
    ]