# Generated by Django 3.2.3 on 2021-06-12 04:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('storages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
