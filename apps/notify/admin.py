from django.contrib import admin

from .models import Prevention, Overdue

# Register your models here.

class PreventionAdmin(admin.ModelAdmin):

    list_display = ('id_sisbase','name','invoice',
            'date','total','ip_address','seeme')

class OverdueAdmin(admin.ModelAdmin):

    list_display = ('id_sisbase','name','pending',
            'ip_address','seeme','removed')

    list_filter = ('pending','seeme', 'removed')

    search_fields = ['name', 'ip_address']

admin.site.register(Prevention, PreventionAdmin)
admin.site.register(Overdue, OverdueAdmin)
