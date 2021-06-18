# Generated by Django 3.2.3 on 2021-06-18 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message="Email must be entered in the format: 'aaaa@kkkk.lll'", regex='^[\\S]{5,30}$')])),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?\\d{9,16}$')])),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('a', 'accepted'), ('d', 'declined'), ('p', 'in process'), ('m', 'on moderation')], default='on moderation', max_length=20)),
            ],
        ),
    ]
