from django import views
from django.urls import path
from .import views
from .views import *

urlpatterns=[
    path('home/',views.home, name='home'),
    path('register/', views.Students_registration, name='Students_registration'),
    path('students/', views.Student_List, name='student_List'),
]