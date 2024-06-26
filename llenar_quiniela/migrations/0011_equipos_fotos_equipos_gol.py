# Generated by Django 3.2.10 on 2024-04-11 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llenar_quiniela', '0010_imagenes_cartas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos_fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(default='NC', max_length=1000000)),
                ('atlas', models.TextField(default='NC', max_length=1000000)),
                ('america', models.TextField(default='NC', max_length=1000000)),
                ('chivas', models.TextField(default='NC', max_length=1000000)),
                ('cruz_azul', models.TextField(default='NC', max_length=1000000)),
                ('tijuana', models.TextField(default='NC', max_length=1000000)),
                ('puebla', models.TextField(default='NC', max_length=1000000)),
                ('queretaro', models.TextField(default='NC', max_length=1000000)),
                ('pumas', models.TextField(default='NC', max_length=1000000)),
                ('toluca', models.TextField(default='NC', max_length=1000000)),
                ('santos', models.TextField(default='NC', max_length=1000000)),
                ('monterrey', models.TextField(default='NC', max_length=1000000)),
                ('tigres', models.TextField(default='NC', max_length=1000000)),
                ('mazatlan', models.TextField(default='NC', max_length=1000000)),
                ('necaxa', models.TextField(default='NC', max_length=1000000)),
                ('san_luis', models.TextField(default='NC', max_length=1000000)),
                ('leon', models.TextField(default='NC', max_length=1000000)),
                ('juarez', models.TextField(default='NC', max_length=1000000)),
                ('pachuca', models.TextField(default='NC', max_length=1000000)),
                ('inter', models.TextField(default='NC', max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos_gol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('atlas', models.CharField(default='1', max_length=1)),
                ('america', models.CharField(default='1', max_length=1)),
                ('chivas', models.CharField(default='1', max_length=1)),
                ('cruz_azul', models.CharField(default='1', max_length=1)),
                ('tijuana', models.CharField(default='1', max_length=1)),
                ('puebla', models.CharField(default='1', max_length=1)),
                ('queretaro', models.CharField(default='1', max_length=1)),
                ('pumas', models.CharField(default='1', max_length=1)),
                ('toluca', models.CharField(default='1', max_length=1)),
                ('santos', models.CharField(default='1', max_length=1)),
                ('monterrey', models.CharField(default='1', max_length=1)),
                ('tigres', models.CharField(default='1', max_length=1)),
                ('mazatlan', models.CharField(default='1', max_length=1)),
                ('necaxa', models.CharField(default='1', max_length=1)),
                ('san_luis', models.CharField(default='1', max_length=1)),
                ('leon', models.CharField(default='1', max_length=1)),
                ('juarez', models.CharField(default='1', max_length=1)),
                ('pachuca', models.CharField(default='1', max_length=1)),
            ],
        ),
    ]
