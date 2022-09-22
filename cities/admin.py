from django.contrib import admin
from cities.models import City
from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    """Add new field to admin model Train"""
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')


admin.site.register(City)
admin.site.register(Train, TrainAdmin)
