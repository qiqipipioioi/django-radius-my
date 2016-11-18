from django.contrib import admin
from userWeb.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'status')
    list_filter = ('status',)
    ordering = ('-created_time',)

admin.site.register(News, NewsAdmin)
# Register your models here.
