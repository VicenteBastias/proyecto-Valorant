# Generated by Django 4.0.6 on 2022-07-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=250)),
                ('pais', models.IntegerField(choices=[(1, 'Chileno'), (2, 'Venenzolano'), (3, 'Haitiano'), (4, 'Colombiano'), (5, 'Otros')])),
                ('edad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['email'],
            },
        ),
    ]