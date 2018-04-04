from django.contrib import admin

from .models import Sensor, SensorReading, Station


class SensorsInline(admin.TabularInline):
    readonly_fields = ('id','station','description','type','last_activity_date')
    model = Sensor

class SensorReadingsInline(admin.TabularInline):
    model = SensorReading
    readonly_fields = ('data','date')

class StationAdmin(admin.ModelAdmin):
    readonly_fields = ('last_activity_date','location_latitude','location_longitude','location_altitude',)
    inlines = [SensorsInline]

class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('id','last_activity_date','station',)
    inlines = [SensorReadingsInline]

class SensorReadingAdmin(admin.ModelAdmin):
    readonly_fields = ('date','data','sensor',)


# Register your models here.
admin.site.register(Station, StationAdmin)
admin.site.register(Sensor,SensorAdmin)
admin.site.register(SensorReading,SensorReadingAdmin)

admin.site.site_header = 'PlayWeather'
