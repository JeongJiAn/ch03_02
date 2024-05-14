from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice2, name='practice2')
]
