from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home2, name='home2'),
    path('chargerXml/', views.chargerXml, name='chargerXml'),
    # path('upload_xml/', views.upload_xml, name='upload_xml'),
    path('create_objects_from_xml/', views.create_objects_from_xml, name='create_objects_from_xml'),
    path('load_events/', views.load_events, name='load_events'),
    path('load_events1/', views.load_events1, name='load_events1'),
    path('load_events2/', views.load_events2, name='load_events2'),
    path('edt_list/', views.edt_list, name='edt_list'),
]