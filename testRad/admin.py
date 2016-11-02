#coding:utf-8
from django.contrib import admin
from testRad.models import Showing, Radcheck, Radusergroup

class ShowingAdmin(admin.ModelAdmin):
    list_display = ('username', 'secret', 'groupname', 'updatetime', 'endtime', 'connections_now', 'connections_limits', 'traffic_now', 'traffic_limits', 'speed_limits')
    readonly_fields = ('username', 'secret', 'groupname', 'updatetime', 'endtime', 'connections_now', 'connections_limits', 'traffic_now', 'traffic_limits', 'speed_limits')
    list_display_links = None
    show_full_result_count = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        if obj is None:     
            return True
        else:              
            return False


class RadcheckAdmin(admin.ModelAdmin):
    list_display = ('username', 'attribute', 'op' ,'value')
    list_editable = ('username', 'attribute', 'op' ,'value')


class RadusergroupAdmin(admin.ModelAdmin):
    list_display = ('username', 'groupname', 'priority', 'updatetime', 'endtime')
    list_editable = ('username', 'groupname', 'priority', 'updatetime', 'endtime')


admin.site.register(Showing, ShowingAdmin)
admin.site.register(Radcheck, RadcheckAdmin)
admin.site.register(Radusergroup, RadusergroupAdmin)
# Register your models here.
