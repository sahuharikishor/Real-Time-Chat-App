from django.urls import path
from . import views


urlpatterns=[
    path('',views.home , name="home.html"),
    path('checkview',views.checkview),
    path('send/',views.send),
    path('getMessages/<str:room>/',views.getMessages),
    path('<str:room>/',views.room,name="room.html"),   
    
]