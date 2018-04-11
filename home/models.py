from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.

class Station(models.Model):
    TIME_TO_WAIT = 60  # Time to wait for activity before declaring station as inactive IN SECONDS

    owner = models.ForeignKey(User,verbose_name="Dueño")
    id = models.CharField(primary_key=True, max_length=255)  # TODO must be unique
    name = models.CharField(max_length=255, unique=True,verbose_name="Nombre")  # TODO must be unique
    location_longitude = models.FloatField(null=True, editable=False,verbose_name="Longitud")
    location_latitude = models.FloatField(null=True, editable=False,verbose_name="Latitud")
    location_altitude = models.FloatField(null=True, editable=False,verbose_name="Altitud")
    last_activity_date = models.DateTimeField(null=True, default=datetime.min, verbose_name="Ultima actividad")
    date_registered = models.DateTimeField(auto_now=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Estacion"
        verbose_name_plural = "Estaciones"

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
    description = models.TextField(blank=True,verbose_name="Descripcion")  # TODO can be null
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='Pluvial',verbose_name="Tipo")
    station = models.ForeignKey(Station, related_name='sensors',verbose_name="Estacion")
    date_registered = models.DateTimeField(auto_now=True, verbose_name="Fecha de registro")
    last_activity_date = models.DateTimeField(null=True, default=datetime.min, verbose_name="Ultima actividad")

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"

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
    date = models.DateTimeField(auto_now=True,verbose_name="Fecha")
    data = models.TextField(default="error")
    sensor = models.ForeignKey(Sensor, related_name="readings")

    class Meta:
        verbose_name = "Lectura"

    def __str__(self):
        return f'Sensor:{self.sensor.id}. Value:{self.data}. at:{self.date} '
