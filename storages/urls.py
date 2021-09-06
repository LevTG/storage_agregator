from django.urls import path
from . import views


urlpatterns = [
    path('', views.StorageRegisterView.as_view()),
    path('<uuid:pk>', views.StorageView.as_view()),
    path('<uuid:pk>/feedbacks', views.GetAllFeedbackView.as_view()),
    path('<uuid:pk>/managers', views.ManagerRegisterView.as_view()),
    path('<uuid:pk>/managers/<str:telegram_id>', views.ManagerView.as_view()),
    path('filter', views.FilterStoragesView.as_view()),
    path('cities', views.GetAllCities.as_view()),
    path('coordinates', views.GetAllStoragesMapView.as_view()),
    path('nearby', views.GetNearbyStoragesMap.as_view()),
    path('fix_url', views.MoveLngLatToLocation.as_view())
]
