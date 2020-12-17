from django.urls import path
from .views import HelloAPIView

urlpatterns = [
    path('hello-view', HelloAPIView.as_view())
]
