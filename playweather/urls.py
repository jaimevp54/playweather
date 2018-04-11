"""playweather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from home.views import *
from api.views import NewReading, ReadReading, NewReadingsBundle
import api.views

api_v1_router = routers.DefaultRouter()
api_v1_router.register(r'stations', api.views.StationViewSet)
api_v1_router.register(r'sensors', api.views.SensorViewSet)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', DashboardPage.as_view(), name='dashboard'),
    url(r'^stations/', StationIndexPage.as_view(), name='station_index'),
    url(r'^station/view/(?P<station_id>[\w]+)$', StationViewPage.as_view(), name='station_view'),
    url(r'^sensors/', SensorIndexPage.as_view(), name='sensor_index'),

    # API
    url(r'^api/v1/',include(api_v1_router.urls)),
    url(r'^api/sensor_reading/new/$', NewReading.as_view(), name='new_reading'),
    url(r'^api/sensor_reading/read/$', ReadReading.as_view(), name='read_reading'),
    url(r'^api/sensor_readings_bundle/new/$', NewReadingsBundle.as_view(), name='new_reading_bundle'),
]
