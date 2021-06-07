from django.urls import path
from . import views


urlpatterns = [
    path('my_company', views.companies),
    path('<int:pk>', views.CompanyView.as_view()),

]
