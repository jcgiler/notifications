#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import os
import django
import codecs

from django.db import IntegrityError, DataError
from sisbase import ip_address

os.sys.path.append('/home/jcgiler/notifications')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
django.setup()

from apps.notify.models import Overdue

UTF8 = codecs.getwriter('utf8')
sys.stdout = UTF8(sys.stdout)

for i in Overdue.objects.all():
    print u'%s;%s;%s' % (i.name, ip_address(i.id_sisbase)['estado'], i.seeme)

