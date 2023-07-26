from django.urls import path
from app3.views import *
app_name='app3'
urlpatterns=[
    path("v31/",v31,name="v31"),
    path("v32/",v32,name="v32"),
    path("v33/",v33,name="v33"),
    
]