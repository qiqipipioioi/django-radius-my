from django.contrib import admin
from radiusServer.models import Nas, NasAttributes, NasShowing


class NasShowingAdmin(admin.ModelAdmin):
    list_display = ('nasname', 'secret', 'type', 'ports', 'now_connections', 'max_connections', 'nas_area', 'vps_supplier', 'vps_endtime')
    readonly_fields = ('nasname', 'secret', 'type', 'ports', 'now_connections', 'max_connections', 'nas_area', 'vps_supplier', 'vps_endtime')
    list_display_links = None
    show_full_result_count = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        if obj is None:     
            return True
        else:              
            return False


class NasAdmin(admin.ModelAdmin):
    list_display = ('nasname', 'shortname', 'type', 'secret' ,'ports', 'server', 'community', 'description')


class NasAttributesAdmin(admin.ModelAdmin):
    list_display = ('nasname', 'max_connections', 'nas_area', 'vps_supplier', 'vps_endtime')


admin.site.register(NasShowing, NasShowingAdmin)
admin.site.register(Nas, NasAdmin)
admin.site.register(NasAttributes, NasAttributesAdmin)
# Register your models here.
