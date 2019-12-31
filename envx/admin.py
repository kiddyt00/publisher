from django.contrib import admin

# Register your models here.

from .models import Env


class EnvAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','change_date','add_date','status']


admin.site.register(Env, EnvAdmin)