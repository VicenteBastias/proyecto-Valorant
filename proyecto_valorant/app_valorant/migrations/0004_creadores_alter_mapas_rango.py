# Generated by Django 4.0.6 on 2022-07-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_valorant', '0003_mapas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rango', models.CharField(choices=[('hierro', 'hierro'), ('bronce', 'bronce'), ('plata', 'plata'), ('oro', 'oro'), ('Platino', 'Platino'), ('Diamante', 'Diamante'), ('ascendente', 'ascendente'), ('inmortal', 'inmortal'), ('radiante', 'radiante')], max_length=30)),
                ('estilo_juego', models.CharField(max_length=30)),
                ('agente_main', models.IntegerField(choices=[(1, 'Fade'), (2, 'Breach'), (3, 'Raze'), (4, 'Chamber'), (5, 'Kay/0'), (6, 'Skye'), (7, 'Cypher'), (8, 'Sova'), (9, 'killjoy'), (10, 'Viper'), (11, 'Phoenix'), (12, 'Astra'), (13, 'Brimstone'), (14, 'Neon'), (15, 'Yoru'), (16, 'Sage'), (17, 'Reyna'), (18, 'Omen'), (19, 'Jett')])),
            ],
        ),
        migrations.AlterField(
            model_name='mapas',
            name='rango',
            field=models.IntegerField(choices=[(1, 'Hierro'), (2, 'Bronce'), (3, 'Plata'), (4, 'Oro'), (5, 'Platino'), (6, 'Diamante'), (7, 'Ascendente'), (8, 'Inmortal'), (9, 'Radiante')]),
        ),
    ]
