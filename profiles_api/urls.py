from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

# Since UserProfileViewSet has a query set, don't assign a basename.
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet, basename='feed')

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
