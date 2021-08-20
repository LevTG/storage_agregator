from django.urls import path
from . import views
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token
from rest_framework_jwt.blacklist.views import BlacklistView

urlpatterns = [
    path('registration', views.UserRegistrationView.as_view(), name='auth_login'),
    # path('auth', obtain_jwt_token),
    path('login', views.ProfileLoginView.as_view()),
    path('logout', BlacklistView.as_view({"post": "create"})),
    # path('logout_all/', views.logout_all, name='auth_logout_all'),
    path('token/refresh', refresh_jwt_token),
    # path('token/verify', verify_jwt_token),
    path('token/verify', views.VerifyTokenView.as_view()),
    path('update/<str:username>/', views.UpdateProfileView.as_view()),
    path('get/<str:username>/', views.FetchUserView.as_view()),
    path('change_password/<str:username>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('change_logo/<str:username>', None),
    path('companies', views.GetAllCompaniesView.as_view()),
    path('applications', views.GetAllApplicationsView.as_view()),
    path('storages', views.GetAllStoragesView.as_view())
]
