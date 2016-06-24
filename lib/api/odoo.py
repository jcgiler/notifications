#!/usr/bin/env python2

import erppeek

SERVER = 'http://openerp.in-planet.net:8069'
DATABASE = 'IN_PLANET'
USERNAME = 'admin'
PASSWORD = '@dminKoru90'

client = erppeek.Client(SERVER, DATABASE, USERNAME, PASSWORD)

#partner = client.read(
#        'res.partner',
#        [('customer', '=', 'True')],
#        ('id', 'name', 'vat_id')
#    )

contract = client.read(
        'ipnt.contract',
        [('state', 'in', ('active','finalized')), ('id', '=', '11142')],
        ('partner_id', 'id_sisbase', 'state'),
    )

print contract
