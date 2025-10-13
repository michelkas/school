from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('liste/', views.students_list, name='students_list'),
]
