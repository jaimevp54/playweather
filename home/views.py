from django.shortcuts import render
from django.views.generic import View

from .models import Station, Sensor
from datetime import datetime, timedelta


# Create your views here.

class DashboardPage(View):
    def get(self, request):
        return render(request, "index.html", context={
            'stations': Station.objects.all(),
            'recent_stations': Station.objects.order_by('date_registered').reverse()[:5],
            'sensors': Sensor.objects.all(),
            'recent_sensors': Sensor.objects.order_by('date_registered').reverse()[:5],
            'active_stations_count': Station.objects.filter(
                last_activity_date__gte=datetime.now() - timedelta(seconds=Station.TIME_TO_WAIT)).count(),
            'active_sensors_count': Sensor.objects.filter(
                last_activity_date__gte=datetime.now() - timedelta(seconds=Sensor.TIME_TO_WAIT)).count()
        })


class StationIndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "station/index.html", context={
            'ROOT_URL': request.get_host(),
            'stations': Station.objects.all()
        })


class SensorIndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "sensor/index.html", context={
            'ROOT_URL': request.get_host(),
            'sensors': Sensor.objects.all(),
            'sensor_types': dict(Sensor.TYPE_CHOICES),
        })


class StationViewPage(View):
    def get(self, request, *args, **kwargs):
        station = Station.objects.get(id=kwargs["station_id"])
        sensors = Sensor.objects.filter(station=station)
        return render(request, "station/view.html", context={
            'ROOT_URL': request.get_host(),
            'station': station,
            'sensors': sensors,
            'sensor_types': dict(Sensor.TYPE_CHOICES),
        })
