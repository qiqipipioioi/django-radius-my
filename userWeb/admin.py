from django.contrib import admin
from userWeb.models import News, userlist


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'status')
    list_filter = ('status',)
    ordering = ('-created_time',)


class userlistAdmin(admin.ModelAdmin):
    list_display = ('username', 'statu')
    list_filter = ('statu',)

admin.site.register(News, NewsAdmin)
admin.site.register(userlist, userlistAdmin)
# Register your models here.
