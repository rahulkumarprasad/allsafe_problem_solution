from django.urls import path
from . import views

urlpatterns=[
    path("",views.HomePage.as_view(),name="home"),
    path("getinfo",views.AllSafeWebInfo.as_view(),name="getinfo"),
    path("getdatewise",views.GetDateWiseData.as_view(),name="getdatewise"),
    
]