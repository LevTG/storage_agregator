# Generated by Django 3.2.3 on 2021-07-26 13:04

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0002_auto_20210630_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
