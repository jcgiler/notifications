#!/usr/bin/env python2

import os
import django
import subprocess

os.sys.path.append('/home/notify/notifications/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
django.setup()

from apps.alert.models import Notify

for i in Notify.objects.all():
    proc = subprocess.check_output(
            '/usr/bin/ssh %(options)s %(user)s@%(router)s -p%(port)s "ip firewall address-list add list=alertas address=%(ip)s"' %
            {
                'user': 'apiuser',
                'router': '172.19.0.1',
                'port': '2200',
                'options': '-o ConnectTimeout=1 -o StrictHostKeyChecking=no',
                'ip': str(i.ip_address)
            }, shell=True
        )
