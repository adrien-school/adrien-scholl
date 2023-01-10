from django.urls import path
from ventehabbi.views import home 

urlpatterns =[
    path('',home,name='kevin'),
]