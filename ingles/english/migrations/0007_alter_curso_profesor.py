# Generated by Django 4.0.4 on 2022-05-19 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0006_alter_curso_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.profesor'),
        ),
    ]
