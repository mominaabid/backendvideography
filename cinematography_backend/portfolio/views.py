# portfolio/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import PortfolioCategory, HeroSlide, Project
from .serializers import PortfolioCategorySerializer, HeroSlideSerializer, ProjectSerializer


class PortfolioCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PortfolioCategory.objects.filter(is_active=True).prefetch_related('projects')
    serializer_class = PortfolioCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['order', 'name']
    search_fields = ['name']
    ordering = ['order']


class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSlide.objects.filter(is_active=True)
    serializer_class = HeroSlideSerializer
    ordering = ['order']


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering = ['order']