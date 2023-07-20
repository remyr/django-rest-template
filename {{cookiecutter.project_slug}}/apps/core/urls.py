from django.urls import path
from .views import StatusAPIView

urlpatterns = [
    path("", StatusAPIView.as_view()),
]
