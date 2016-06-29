#!/usr/bin/env python2

import os
import django
import erppeek

from django.db import IntegrityError
from sisbase import ip_address

os.sys.path.append('/home/notify/notifications/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
django.setup()

from apps.alert.models import Notify

SERVER = 'http://openerp.in-planet.net:8069'
DATABASE = 'IN_PLANET'
USERNAME = 'admin'
PASSWORD = '@dminKoru90'

client = erppeek.Client(SERVER, DATABASE, USERNAME, PASSWORD)

# Default args:
# client.read(obj, domain, fields=None, offset=0, limit=None, order=None, context=None)

invoice = client.read(
        'account.invoice',
        [
            ('date_due','=','2016-06-30'),
            ('type','=','out_invoice'),
            ('state','=','open'),
            ('origin','like','Contrato%')
        ],
        ('partner_id','number','amount_total','date_due'),
        limit=3
    )

contract = client.model('ipnt.contract')

for ids in invoice:

    id_sisbase = contract.get([('partner_id','=',ids['partner_id'][0])]).id_sisbase

    try:
        rec = Notify(
                id_sisbase = id_sisbase,
                name = ids['partner_id'][1].strip().title(),
                invoice = ids['number'],
                date = ids['date_due'],
                total = ids['amount_total'],
                ip_address = str(ip_address(id_sisbase)['ip'])
            )

        rec.save()

    except IntegrityError:
        pass
