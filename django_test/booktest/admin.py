from django.contrib import admin

from .models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['id', 'btitle']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
