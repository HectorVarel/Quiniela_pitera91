# Generated by Django 3.2.10 on 2024-05-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llenar_quiniela', '0011_equipos_fotos_equipos_gol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos_pendientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j1', models.TextField(default='NC', max_length=1000000)),
                ('j2', models.TextField(default='NC', max_length=1000000)),
                ('j3', models.TextField(default='NC', max_length=1000000)),
                ('j4', models.TextField(default='NC', max_length=1000000)),
                ('j5', models.TextField(default='NC', max_length=1000000)),
                ('j6', models.TextField(default='NC', max_length=1000000)),
                ('j7', models.TextField(default='NC', max_length=1000000)),
                ('j8', models.TextField(default='NC', max_length=1000000)),
                ('j9', models.TextField(default='NC', max_length=1000000)),
                ('j10', models.TextField(default='NC', max_length=1000000)),
                ('j11', models.TextField(default='NC', max_length=1000000)),
                ('j12', models.TextField(default='NC', max_length=1000000)),
                ('j13', models.TextField(default='NC', max_length=1000000)),
                ('j14', models.TextField(default='NC', max_length=1000000)),
                ('j15', models.TextField(default='NC', max_length=1000000)),
                ('j16', models.TextField(default='NC', max_length=1000000)),
                ('j17', models.TextField(default='NC', max_length=1000000)),
            ],
        ),
    ]
