from django.contrib import admin
from testRad.models import Showing, Radcheck, Radusergroup

class ShowingAdmin(admin.ModelAdmin):
    list_display = ('username', 'secret', 'groupname', 'connections_now', 'connections_limits', 'traffic_now', 'traffic_limits', 'speed_limits')
    readonly_fields = ('username', 'secret', 'groupname', 'connections_now', 'connections_limits', 'traffic_now', 'traffic_limits', 'speed_limits')
    list_display_links = None
    show_full_result_count = True


admin.site.register(Showing, ShowingAdmin)
admin.site.register(Radcheck)
admin.site.register(Radusergroup)
# Register your models here.
