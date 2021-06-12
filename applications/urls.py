from django.urls import path
from . import views

urlpatterns = [
    path('add', views.my_application),
    # path('get_first', views.get_first),
    path('get_all', views.get_all_applications),
]
