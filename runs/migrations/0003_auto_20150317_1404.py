# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0002_auto_20150310_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categorías', 'verbose_name': 'categoría'},
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'verbose_name_plural': 'carreras', 'verbose_name': 'carrera'},
        ),
        migrations.AlterModelOptions(
            name='runner',
            options={'verbose_name_plural': 'corredores', 'verbose_name': 'corredor'},
        ),
        migrations.AddField(
            model_name='run',
            name='categories',
            field=models.ManyToManyField(to='runs.Category', verbose_name='categoría'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='nationality',
            field=django_countries.fields.CountryField(verbose_name='pais de naciomiento', max_length=2),
            preserve_default=True,
        ),
    ]
