from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
# Since UserProfileViewSet has a query set, don't assign a basename.
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('', include(router.urls))
]
