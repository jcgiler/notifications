#!/usr/bin/env python2

import os
import django

from django.db import IntegrityError, DataError
from sisbase import ip_address

os.sys.path.append('/home/jcgiler/notifications')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
django.setup()

from apps.notify.models import Overdue

csv = open('query.csv').read().splitlines()

for i in csv:

    c = i.split(';')
    id_sisbase = c[0]
    ip = [ ip_address(id_sisbase)[x] for x in ['ip','estado'] ]

    if ip[1] == 'activo':
        c.append(ip[0])

        try:
             rec = Overdue(
                     id_sisbase = c[0],
                     name = c[1],
                     pending = c[2],
                     ip_address = c[3]
                 )

             rec.save()

        except DataError:
            pass
        except IntegrityError:
            pass
