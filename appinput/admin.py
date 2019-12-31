from django.contrib import admin
# Register your models here.
from .models import App

class AppAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','change_date','add_date','git_url']

admin.site.register(App, AppAdmin)
