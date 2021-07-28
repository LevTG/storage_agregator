from django.urls import path
from . import views


urlpatterns = [
    path('<int:album_id>', views.ImageRegisterView.as_view()),
    path('<int:album_id>/<int:image_id>', views.ImageView.as_view()),
]
