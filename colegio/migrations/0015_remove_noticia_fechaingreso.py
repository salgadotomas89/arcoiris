# Generated by Django 3.2.8 on 2021-11-17 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0014_rename_fecha_noticia_fechaingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='fechaIngreso',
        ),
    ]
