# Generated by Django 4.0.6 on 2022-07-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_valorant', '0002_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='mapas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idusuario', models.CharField(max_length=30)),
                ('mapa', models.IntegerField(choices=[(1, 'Bind'), (2, 'Ice box'), (3, 'Split'), (4, 'Fracture'), (5, 'Heaven'), (6, 'Acent'), (7, 'Breeze'), (8, 'Pearl')])),
                ('aliminaciones', models.CharField(max_length=2)),
                ('muertes', models.CharField(max_length=2)),
                ('agente', models.IntegerField(choices=[(1, 'Fade'), (2, 'Breach'), (3, 'Raze'), (4, 'Chamber'), (5, 'Kay/0'), (6, 'Skye'), (7, 'Cypher'), (8, 'Sova'), (9, 'killjoy'), (10, 'Viper'), (11, 'Phoenix'), (12, 'Astra'), (13, 'Brimstone'), (14, 'Neon'), (15, 'Yoru'), (16, 'Sage'), (17, 'Reyna'), (18, 'Omen'), (19, 'Jett')])),
                ('rango', models.IntegerField(choices=[(1, 'Fade'), (2, 'Breach'), (3, 'Raze'), (4, 'Chamber'), (5, 'Kay/0'), (6, 'Skye'), (7, 'Cypher'), (8, 'Sova'), (9, 'killjoy'), (10, 'Viper'), (11, 'Phoenix'), (12, 'Astra'), (13, 'Brimstone'), (14, 'Neon'), (15, 'Yoru'), (16, 'Sage'), (17, 'Reyna'), (18, 'Omen'), (19, 'Jett')])),
                ('imagen', models.ImageField(upload_to='mapas')),
            ],
        ),
    ]
