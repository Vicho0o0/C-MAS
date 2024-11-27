# Generated by Django 5.1.1 on 2024-11-27 20:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horario', models.CharField(max_length=50)),
                ('Actividad', models.CharField(max_length=50)),
                ('Maquinas_Diponibles', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('plan', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoMuscular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'GrupoMuscular',
                'verbose_name_plural': 'GruposMusculares',
                'db_table': 'grupomuscular',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Membresias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Precio', models.IntegerField(default=0)),
                ('Horario1', models.CharField(max_length=50)),
                ('Horario2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MetricasCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(max_length=12, unique=True)),
                ('altura', models.IntegerField(null=True)),
                ('peso', models.IntegerField(null=True)),
                ('horas_entrenadas', models.IntegerField(null=True)),
                ('fecha_marca', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'TipoEjercicio',
                'verbose_name_plural': 'TipoEjercicios',
                'db_table': 'tipoejercicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('grupo_muscular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortalCMAS.grupomuscular')),
                ('tipo_ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortalCMAS.tipoejercicio')),
            ],
            options={
                'verbose_name': 'Ejercicios',
                'verbose_name_plural': 'Ejercicios',
                'db_table': 'ejercicios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MetricasEjerciciosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(max_length=12, unique=True)),
                ('peso', models.IntegerField(null=True)),
                ('repeticiones', models.IntegerField(null=True)),
                ('fecha_marca', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortalCMAS.ejercicios')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PortalCMAS.perfil')),
            ],
        ),
    ]
