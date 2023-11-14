from django.contrib import admin
from .models import *
# Register your models here.

# class SubUrlsInline(admin.StackedInline):
#     model = SubUrls
#     # max_num = 2
#     extra = 0

# class UrlsAdmin(admin.ModelAdmin):
#     inlines = [SubUrlsInline,]

admin.site.register(Urls)