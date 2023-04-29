from django.contrib import admin
from .models import City

#admin.site.register(City)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_per_page = 20
    