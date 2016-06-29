from django.shortcuts import render
from .models import Notify
from ipware.ip import get_ip

# Create your views here.

def Content(request):

    ip = get_ip(request)
    context = Notify.objects.get(ip_address=str(ip))
    context.seeme = context.seeme + 1
    context.save()
    template = 'alert/content.html'

    return render(request, template,
            { 'item': context, 'name': context.name.split(' ')[0] })
