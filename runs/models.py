# coding=utf-8

from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):
    """
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'


class Run(models.Model):
    """
    """
    date = models.DateTimeField('fecha')
    quota = models.PositiveIntegerField('cupo')
    place = models.CharField('lugar', max_length=32)
    distance = models.CharField('distancia', max_length=32)
    price = models.DecimalField('precio', max_digits=6, decimal_places=2)
    banner = models.ImageField('banner', upload_to='banners')
    payment_method = models.CharField('método de pago', max_length=32)
    payment_place = models.CharField('lugar de pago', max_length=32)
    categories = models.ManyToManyField(Category, verbose_name='categorías')

    def __str__(self):
        return '{} - {}'.format(self.date.strftime('%Y/%m/%d - %H:%M'), self.distance)

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'


class Runner(models.Model):
    """
    """
    GENDER_CHOICES = (
        (1, 'Masculino'),
        (2, 'Femenino')
    )
    SIZE_CHOICES = (
        (1, 'XS'),
        (2, 'S'),
        (3, 'M'),
        (4, 'L'),
        (5, 'XL'),
        (6, 'XXL'),
    )
    run = models.ForeignKey(Run, related_name='runners', verbose_name='carrera')
    firstname = models.CharField('nombre/s', max_length=64)
    lastname = models.CharField('apellido/s', max_length=64)
    document = models.CharField('n° de documento', max_length=32)
    birthday = models.DateField('fecha de nacimiento')
    gender = models.PositiveIntegerField('sexo', choices=GENDER_CHOICES)
    nationality = CountryField('pais de naciomiento')
    address = models.CharField('dirección', max_length=64)
    phone = models.CharField('teléfono', max_length=64)
    emergency_contact = models.CharField('contacto de emergencia', max_length=64)
    email = models.EmailField('correo elecrónico')
    group = models.CharField('agrupación', max_length=64)
    category = models.ForeignKey(Category, related_name='runners_category', verbose_name='categoría')
    size = models.PositiveIntegerField('talle de remera', choices=SIZE_CHOICES)

    def __str__(self):
        return '{} - {} {}'.format(self.document, self.firstname, self.lastname)

    class Meta:
        verbose_name = 'corredor'
        verbose_name_plural = 'corredores'

