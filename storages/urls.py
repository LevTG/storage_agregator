from django.urls import path
from . import views


urlpatterns = [
    path('storages', views.storage)
]
