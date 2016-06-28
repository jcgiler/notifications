from django.contrib import admin

from .models import Notify

# Register your models here.

class NotifyAdmin(admin.ModelAdmin):

    list_display = ('id_sisbase','name','invoice',
            'date','total','ip_address','seeme')

admin.site.register(Notify, NotifyAdmin)
