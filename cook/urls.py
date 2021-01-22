from django.urls import path

from . import views

urlpatterns = [
    path('temp_response', views.temp_response),
]