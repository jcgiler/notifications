import subprocess
from django.shortcuts import render, Http404
from .models import Notify
from ipware.ip import get_ip

# Create your views here.

def Content(request):

    try:
        ip = get_ip(request)
        context = Notify.objects.get(ip_address=str(ip))
        context.seeme = context.seeme + 1
        context.save()
        template = 'alert/content.html'

        if context.seeme >= 5:
            context.delete()

        return render(request, template,
                { 'item': context, 'name': context.name.split(' ')[0] })

        proc = subprocess.check_output(
                '/usr/bin/ssh %(options)s %(user)s@%(router)s -p%(port)s "ip firewall address-list remove [find address=%(ip)s]"' %
                {
                    'user': 'apiuser',
                    'router': '192.168.1.1',
                    'port': '2200',
                    'options': '-o ConnectTimeout=1 -o StrictHostKeyChecking=no',
                    'ip': str(ip)
                }, shell=True
            )

    except Notify.DoesNotExist:
        raise Http404('No existe')
