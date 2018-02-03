from rest_framework import serializers

from home.models import Station, Sensor, SensorReading


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'description', 'type', 'station')


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'owner', 'name')


class SensorReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorReading
        fields = ('date', 'data', 'sensor')
