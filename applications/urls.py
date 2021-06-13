from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationRegistrationView.as_view()),
    path('<uuid:id>', views.SingleApplicationView.as_view()),
    # path('get_first', views.get_first),
    # path('get_all', views.get_all_applications),
]
