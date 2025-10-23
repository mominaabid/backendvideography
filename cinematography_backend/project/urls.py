# cinematography_backend/project/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioHeroViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'portfolio-hero', PortfolioHeroViewSet, basename='portfolio-hero')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]