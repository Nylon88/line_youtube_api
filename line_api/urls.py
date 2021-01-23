from django.urls import path

from . import views


urlpatterns = [
    path('message',views.message),
    path('linehook',views.LineHook.as_view()),
]