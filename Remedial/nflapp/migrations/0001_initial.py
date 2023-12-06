# Generated by Django 4.2.7 on 2023-12-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dueño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nflapp.dueño')),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('capacidad', models.IntegerField()),
                ('tamaño', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('posicion', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nflapp.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nflapp.equipo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='estadio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nflapp.estadio'),
        ),
    ]
