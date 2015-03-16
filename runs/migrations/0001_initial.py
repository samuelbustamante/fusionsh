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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('quota', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=32)),
                ('distance', models.CharField(max_length=32)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('banner', models.ImageField(upload_to='banners')),
                ('payment_method', models.CharField(max_length=32)),
                ('payment_place', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('document', models.CharField(max_length=32)),
                ('birthday', models.DateField()),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')])),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('emergency_contact', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=75)),
                ('group', models.CharField(max_length=64)),
                ('size', models.PositiveIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')])),
                ('category', models.ForeignKey(to='runs.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
