# Generated by Django 4.0.4 on 2022-05-11 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0002_alter_profesor_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=500)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.profesor')),
            ],
        ),
    ]