from django.urls import path, include
from rest_framework.routers import DefaultRouter
from demo_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('users-list', views.UserListAPI.as_view()),
    path('user-detail/<int:pk>/', views.UserDetailView.as_view()),
    path('', include(router.urls)),
]


