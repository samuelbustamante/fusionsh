# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'categorías',
                'verbose_name': 'categoría',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='fecha')),
                ('quota', models.PositiveIntegerField(verbose_name='cupo')),
                ('place', models.CharField(max_length=32, verbose_name='lugar')),
                ('distance', models.CharField(max_length=32, verbose_name='distancia')),
                ('price', models.DecimalField(max_digits=6, decimal_places=2, verbose_name='precio')),
                ('banner', models.ImageField(upload_to='banners', verbose_name='banner')),
                ('payment_method', models.CharField(max_length=32, verbose_name='método de pago')),
                ('payment_place', models.CharField(max_length=32, verbose_name='lugar de pago')),
            ],
            options={
                'verbose_name_plural': 'carreras',
                'verbose_name': 'carrera',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='nombre/s')),
                ('lastname', models.CharField(max_length=64, verbose_name='apellido/s')),
                ('document', models.CharField(max_length=32, verbose_name='n° de documento')),
                ('birthday', models.DateField(verbose_name='fecha de nacimiento')),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], verbose_name='sexo')),
                ('nationality', django_countries.fields.CountryField(max_length=2, verbose_name='pais de naciomiento')),
                ('address', models.CharField(max_length=64, verbose_name='dirección')),
                ('phone', models.CharField(max_length=64, verbose_name='teléfono')),
                ('emergency_contact', models.CharField(max_length=64, verbose_name='contacto de emergencia')),
                ('email', models.EmailField(max_length=75, verbose_name='correo elecrónico')),
                ('group', models.CharField(max_length=64, verbose_name='agrupación')),
                ('size', models.PositiveIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], verbose_name='talle de remera')),
                ('category', models.ForeignKey(to='runs.Category', verbose_name='categoría', related_name='runners_category')),
                ('run', models.ForeignKey(to='runs.Run', verbose_name='carrera', related_name='runners')),
            ],
            options={
                'verbose_name_plural': 'corredores',
                'verbose_name': 'corredor',
            },
            bases=(models.Model,),
        ),
    ]
