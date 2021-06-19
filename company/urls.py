from django.urls import path
from . import views


urlpatterns = [
    path('', views.CompanyRegisterView.as_view()),
    path('<uuid:id>/storages', views.GetAllStorages.as_view()),
    path('<uuid:id>', views.SingleCompanyView.as_view()),

]
