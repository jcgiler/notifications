import subprocess
from django.shortcuts import render, Http404
from .models import Prevention, Overdue
from ipware.ip import get_ip

# Create your views here.

def Content(request):

    ip = str(get_ip(request))

    try:
        context = Overdue.objects.get(ip_address=ip)
        template = 'notify/content.html'

        return render(request, template,
                { 'item': context, 'name': context.name.split(' ')[0] })

    except Overdue.DoesNotExist:
        raise Http404('No existe')


def Confirm(request):

    ip = str(get_ip(request))

    config = {
                'user': 'apiuser',
                'router': '172.19.0.1',
                'port': '2200',
                'options': '-o ConnectTimeout=1 -o StrictHostKeyChecking=no',
                'ip': ip,
                'rule': 'ip firewall address-list remove [find address=%s]' % ip
            }

    context = Overdue.objects.get(ip_address=config['ip'])

    if context.seeme < 30:

            proc = subprocess.check_output(
                    '/usr/bin/ssh %(options)s %(user)s@%(router)s -p %(port)s "%(rule)s"' % config,
                    shell=True
                )

            context.seeme = context.seeme + 1
            context.removed = True
            context.save()

    return True
