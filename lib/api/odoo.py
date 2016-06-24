#!/usr/bin/env python2

import erppeek
from sisbase import ip_address

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
            ('date_due','=','2016-06-29'),
            ('type','=','out_invoice'),
            ('state','=','open'),
            ('origin','like','Contrato%')
        ],
        ('partner_id','number','amount_total','date_due'),
        limit=3
    )

contract = client.model('ipnt.contract')

data = {}

for ids in invoice:
    data['name'] = ids['partner_id'][1].strip().title()
    data['invoice'] = ids['number']
    data['total'] = ids['amount_total']
    data['date'] = ids['date_due']
    id_sisbase = contract.get([('partner_id','=',ids['partner_id'][0])]).id_sisbase
    data['id_sisbase'] = id_sisbase
    data['ip_address'] = str(ip_address(id_sisbase)['ip'])

    print data
