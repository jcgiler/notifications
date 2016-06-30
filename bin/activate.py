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

for i in Overdue.objects.all():

    config['ip'] = str(i.ip_address)
    config['rule'] = 'ip firewall address-list add list=vencidos address=%s' % config['ip']

    if i.seeme < 30:
	try:
        	proc = subprocess.check_output(
                	'/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
                	shell=True
            	)
	except subprocess.CalledProcessError:
		pass
