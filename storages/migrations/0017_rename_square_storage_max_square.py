# Generated by Django 3.2.3 on 2021-08-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storages', '0016_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='square',
            new_name='max_square',
        ),
    ]
