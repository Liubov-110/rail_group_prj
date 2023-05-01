from django.contrib import admin
from .models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_city', 'end_city', 'travel_time']

admin.site.register(Route, RouteAdmin)
