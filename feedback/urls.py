from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackRegistrationView.as_view()),
    path('<uuid:pk>', views.FeedbackView.as_view()),
    path('answer', views.AnswerRegistrationView.as_view()),
    path('answer/<uuid:pk>', views.AnswerView.as_view()),
    path('review', views.ReviewRegisterView.as_view())
    ]
