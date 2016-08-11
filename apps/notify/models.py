from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Prevention(models.Model):

    id_sisbase = models.IntegerField('ID Sisbase', unique=True)
    name = models.CharField('Nombres', max_length=255)
    invoice = models.CharField('Numero Factura', max_length=40)
    date = models.DateField('Fecha Maxima')
    total = models.DecimalField('Valor Factura', max_digits=6, decimal_places=2)
    ip_address = models.GenericIPAddressField('Ip', protocol='ipv4')
    seeme = models.PositiveSmallIntegerField('Visto', blank=True, null=True, default=0)

    def __unicode__(self):
        return self.name

class Overdue(models.Model):

    id_sisbase = models.IntegerField('ID Sisbase', unique=True)
    name = models.CharField('Nombres', max_length=255)
    cid = models.CharField('Cedula', max_length=40, null=True, blank=True)
    pending = models.PositiveSmallIntegerField('Facturas Pendientes')
    residual = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True) 
    ip_address = models.GenericIPAddressField('Ip', protocol='ipv4')
    seeme = models.PositiveSmallIntegerField('Visto', blank=True, null=True, default=0)
    removed = models.BooleanField('Regla Removida', default=True)

    def delete(self):
        from bin.sync import config
        import subprocess

        config['ip'] = self.ip_address
        config['rule'] = 'ip firewall address-list remove [find address=%s]' % config['ip']

        proc = subprocess.call(
               '/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
               shell=True
               )

        super(Overdue, self).delete()

        print '%s Removed' % config['ip']

    def __unicode__(self):
        return self.name
