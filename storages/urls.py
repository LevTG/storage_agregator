from django.urls import path
from . import views


urlpatterns = [
    path('', views.StorageRegisterView.as_view()),
    path('<uuid:pk>', views.StorageView.as_view()),
    path('filter', views.FilterStoragesView.as_view()),
    path('cities', views.GetAllCities.as_view()),
    path('coordinates', views.GetAllStoragesMap.as_view()),
    path('nearby', views.GetNearbyStoragesMap.as_view())
]
