#!/usr/bin/env python2

import os
import django
import subprocess

os.sys.path.append('/home/jcgiler/notifications/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
django.setup()

from apps.notify.models import Prevention, Overdue

config = {
            'user': 'apiuser',
            'router': '172.19.0.1',
            'port': '2200',
            'options': '-o ConnectTimeout=1 -o StrictHostKeyChecking=no',
            'ip': None,
            'rule': None
        }


try:

    config['rule'] = 'ip firewall address-list print where list=vencidos'

    proc = subprocess.check_output(
        '/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
        shell=True
    )

    router = [ i.split() for i in proc.strip(' \t\n\r').splitlines() ]

    list_ip_db = [ i.ip_address for i in Overdue.objects.all() ]

    for i in router:

        if i[2] not in list_ip_db:

            config['ip'] = i[2]
            config['rule'] = 'ip firewall address-list remove [find address=%s]' % config['ip']

            proc = subprocess.check_output(
                '/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
                shell=True
            )

            print '%s Removed' % config['ip']

except subprocess.CalledProcessError:
	pass
