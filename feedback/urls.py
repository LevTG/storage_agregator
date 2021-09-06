from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackRegistrationView.as_view()),
    path('<uuid:pk>', views.SingleFeedbackView.as_view()),
]
