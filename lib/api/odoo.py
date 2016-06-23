#!/usr/bin/env python2

import xmlrpclib as Client

url = 'http://openerp.in-planet.net:8069'
db = 'IN_PLANET'
user = 'admin'
password = '@dminKoru90'

common = Client.ServerProxy('%s/xmlrpc/2/common' % url)
common.version()
