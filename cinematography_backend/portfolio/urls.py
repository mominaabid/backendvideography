# portfolio/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioCategoryViewSet, HeroSlideViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'categories', PortfolioCategoryViewSet, basename='portfolio_category')
router.register(r'hero-slides', HeroSlideViewSet, basename='hero_slide')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]