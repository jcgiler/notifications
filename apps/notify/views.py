import subprocess
from django.shortcuts import render, Http404
from .models import Prevention, Overdue
from ipware.ip import get_ip

# Create your views here.

def Content(request):

    ip = get_ip(request)

    config = {
                'user': 'apiuser',
                'router': '172.19.0.1',
                'port': '2200',
                'options': '-o ConnectTimeout=1 -o StrictHostKeyChecking=no',
                'ip': ip,
                'rule': 'ip firewall address-list remove [find address=%s]' % ip
            }

    try:
        context = Overdue.objects.get(ip_address=config['ip'])

        if context.seeme < 30:
            context.seeme = context.seeme + 1
            context.save()

        template = 'notify/content.html'

        proc = subprocess.check_output(
                '/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
                shell=True
            )

        return render(request, template,
                { 'item': context, 'name': context.name.split(' ')[0] })

    except Overdue.DoesNotExist:
        raise Http404('No existe')
