from django.urls import path
from .views import *

urlpatterns= [
   path('',login_auth ,name='login'),
   path('article/<object>' ,login_auth,name='login1'),
   path('register/',register ,name="register") ,
   path('logout', logouts, name='lagouts')
]