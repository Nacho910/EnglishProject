# Generated by Django 4.0.4 on 2022-05-05 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
