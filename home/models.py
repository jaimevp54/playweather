from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.

class Station(models.Model):
    TIME_TO_WAIT = 60  # Time to wait for activity before declaring station as inactive IN SECONDS

    owner = models.ForeignKey(User)
    id = models.CharField(primary_key=True, max_length=255)  # TODO must be unique
    name = models.CharField(max_length=255, unique=True)  # TODO must be unique
    location_longitude = models.FloatField(null=True, editable=False)
    location_latitude = models.FloatField(null=True, editable=False)
    location_altitude = models.FloatField(null=True, editable=False)
    last_activity_date = models.DateTimeField(null=True, default=datetime.min)
    date_registered = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estacion"

    @property
    def sensor_count(self):
        return len(self.sensor_set)

    def __str__(self):
        return f'{self.name} - Owner: {self.owner.username}'


class Sensor(models.Model):
    TIME_TO_WAIT = 60  # Time to wait for activity before declaring sensor as inactive IN SECONDS
    TYPE_CHOICES = [
        ('P', 'Pluvial'),
        ('WS', 'Velocidad Viento'),
        ('WD', 'Direccion Viento'),
        ('UV', 'Ultra Violeta'),
        ('TEMP', 'Temperatura'),
        ('HUM', 'Humedad'),
        ('CO', 'CO'),
        ('CO2', 'CO2')
    ]
    id = models.CharField(primary_key=True, max_length=255)
    description = models.TextField(blank=True)  # TODO can be null
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='Pluvial')

    station = models.ForeignKey(Station, related_name='sensors')
    date_registered = models.DateTimeField(auto_now=True)
    last_activity_date = models.DateTimeField(null=True, default=datetime.min)

    class Meta:
        verbose_name = "Sensor"

    @property
    def measurement_unit(self):
        return {
            'P': 'mm',
            'WS': 'KM/h',
            'WD': '',
            'UV': '',
            'TEMP': '°C',
            'HUM': '%',
            'CO': 'ppm',
            'CO2': 'ppm'
        }[self.type]

    def __str__(self):
        return f'{self.id} - Installed at: {self.station.name}'


class SensorReading(models.Model):
    date = models.DateTimeField(auto_now=True)
    data = models.TextField(default="error")
    sensor = models.ForeignKey(Sensor, related_name="readings")

    class Meta:
        verbose_name = "Lectura"

    def __str__(self):
        return f'Sensor:{self.sensor.id}. Value:{self.data}. at:{self.date} '
