# Generated by Django 3.2.3 on 2021-06-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_carry',
            field=models.DateField(blank=True, null=True),
        ),
    ]
