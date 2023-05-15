from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home , name='home'),
    path('login', views.login, name='login'),
    path('register' , views.register , name='register'),
    path('mycollection/create' , views.create , name='create'),
    path('mycollection/update' , views.update , name='update'),
    path('mycollection' , views.mycollection , name='mycollection'),
    path('home/infopiece' , views.infopiece , name='infopiece'),

]
