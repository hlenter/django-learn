from django.contrib import admin

from .models import *


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'gender',  'hcontent']
    list_filter = ['hname']
    search_fields = ['id', 'hname']


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['id', 'btitle']
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
