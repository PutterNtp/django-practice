from django.urls import path
from django.conf.urls import url
from appTwo import views

urlpatterns = [
    path('',views.users,name='user'),
    
]
