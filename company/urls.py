from django.urls import path
from . import views


urlpatterns = [
    path('', views.CompanyRegisterView.as_view()),
    path('<uuid:pk>/storages', views.GetAllStorages.as_view()),
    path('<uuid:pk>/logo', views.LogoView.as_view()),
    path('<uuid:pk>', views.SingleCompanyView.as_view()),
    path('companies', views.GetAllCompanies.as_view())
]
