from django.urls import path
from . import views


urlpatterns = [
    path('', views.StorageRegisterView.as_view()),
    path('<uuid:pk>', views.StorageView.as_view())
]
