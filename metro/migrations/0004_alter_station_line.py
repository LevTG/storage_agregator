# Generated by Django 3.2.3 on 2021-08-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0003_alter_line_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='metro.line'),
        ),
    ]
