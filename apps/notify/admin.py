from django.contrib import admin

from .models import Prevention

# Register your models here.

class PreventionAdmin(admin.ModelAdmin):

    list_display = ('id_sisbase','name','invoice',
            'date','total','ip_address','seeme')

admin.site.register(Prevention, PreventionAdmin)
