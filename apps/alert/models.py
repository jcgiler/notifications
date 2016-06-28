from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Notify(models.Model):

    id_sisbase = models.IntegerField('ID Sisbase')
    name = models.CharField('Nombres', max_length=255)
    invoice = models.CharField('Numero Factura', max_length=40)
    date = models.DateField('Fecha Maxima')
    total = models.DecimalField('Valor Factura', max_digits=6, decimal_places=2)
    ip_address = models.GenericIPAddressField('Ip', protocol='ipv4')

    def __str__(self):
        return self.name
