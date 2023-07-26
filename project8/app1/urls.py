from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path("v11/",v11,name="v11"),
    path("v12/",v12,name="v12"),
    path("v13/",v13,name="v13"),
    path("v14/",v14,name="v14"),
    
]