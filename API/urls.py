from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'api', StudentViewSet, basename='api')
# urlpatterns = router.urls

urlpatterns = [
    path('', StudentView.as_view()),
    path('<int:pk>/', StudentView.as_view()),
]
