from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path("v21/",v21,name="v21"),
    path("v22/",v22,name="v22"),
    path("v23/",v23,name="v23"),
    
]