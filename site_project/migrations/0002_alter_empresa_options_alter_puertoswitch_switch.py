# Generated by Django 5.0.2 on 2024-03-01 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterField(
            model_name='puertoswitch',
            name='switch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.switch', verbose_name='Switch'),
        ),
    ]