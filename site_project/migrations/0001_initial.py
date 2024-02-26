# Generated by Django 5.0.2 on 2024-02-26 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Patch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Patch',
                'verbose_name_plural': 'Patchs',
            },
        ),
        migrations.CreateModel(
            name='PuertoSwitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
            ],
            options={
                'verbose_name': 'PuertoSwitch',
                'verbose_name_plural': 'PuertosSwitch',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Switch',
                'verbose_name_plural': 'Switchs',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='Ip')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.area', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Maquina',
                'verbose_name_plural': 'Maquinas',
            },
        ),
        migrations.CreateModel(
            name='PuertoPatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('patch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.patch', verbose_name='Patch')),
                ('puerto_switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.puertoswitch', verbose_name='Puerto Switch')),
            ],
            options={
                'verbose_name': 'PuertoPatch',
                'verbose_name_plural': 'PuertosPatch',
            },
        ),
        migrations.AddField(
            model_name='puertoswitch',
            name='switch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_project.switch', verbose_name='Puerto Switch'),
        ),
    ]
