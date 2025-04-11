from django.urls import path
from . views import *
urlpatterns = [
    path('layout/',layout,name='layout'),
    path('',home,name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('services/',services,name='services'),
    path('projects/',projects,name='projects'),
    path('logcode/',logcode,name='logcode'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',logout_view,name='logout'),

]
