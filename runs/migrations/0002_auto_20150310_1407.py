# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='run',
            field=models.ForeignKey(default=1, to='runs.Run', verbose_name='carrera', related_name='runners'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='banner',
            field=models.ImageField(verbose_name='banner', upload_to='banners'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='date',
            field=models.DateTimeField(verbose_name='fecha'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='distance',
            field=models.CharField(verbose_name='distancia', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='payment_method',
            field=models.CharField(verbose_name='método de pago', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='payment_place',
            field=models.CharField(verbose_name='lugar de pago', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='place',
            field=models.CharField(verbose_name='lugar', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='price',
            field=models.DecimalField(verbose_name='precio', decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='quota',
            field=models.PositiveIntegerField(verbose_name='cupo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='address',
            field=models.CharField(verbose_name='dirección', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='birthday',
            field=models.DateField(verbose_name='fecha de nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='category',
            field=models.ForeignKey(to='runs.Category', verbose_name='categoría', related_name='runners_category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='document',
            field=models.CharField(verbose_name='n° de documento', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='email',
            field=models.EmailField(verbose_name='correo elecrónico', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='emergency_contact',
            field=models.CharField(verbose_name='contacto de emergencia', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='firstname',
            field=models.CharField(verbose_name='nombre/s', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='gender',
            field=models.PositiveIntegerField(verbose_name='sexo', choices=[(1, 'Masculino'), (2, 'Femenino')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='group',
            field=models.CharField(verbose_name='agrupación', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='lastname',
            field=models.CharField(verbose_name='apellido/s', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='nationality',
            field=django_countries.fields.CountryField(verbose_name='nacionalidad', max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='phone',
            field=models.CharField(verbose_name='teléfono', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='size',
            field=models.PositiveIntegerField(verbose_name='talle de remera', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')]),
            preserve_default=True,
        ),
    ]
