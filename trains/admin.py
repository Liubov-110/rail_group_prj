from django.contrib import admin
from .models import Train


admin.site.register(Train)
# @admin.register(Train)
# class TrainAdmin(admin.ModelAdmin):
    #list_display = ('code', 'start_city', 'end_city', 'travel_time')
