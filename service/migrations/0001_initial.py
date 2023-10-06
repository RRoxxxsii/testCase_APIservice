# Generated by Django 4.2.5 on 2023-10-05 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('mobile', models.CharField(max_length=255, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='service.employee', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_visited', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField(verbose_name='Ширина')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='service.store', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
            },
        ),
    ]