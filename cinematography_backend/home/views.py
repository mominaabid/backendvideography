# home/views.py

from rest_framework import viewsets, filters
from .models import HomeHero, HomeStat, HomeIntro, HomeSkill, HomeService, HomeProcess, HomeTool, HomeFAQ, HomeCTA
from .serializers import HomeHeroSerializer, HomeStatSerializer, HomeIntroSerializer, HomeSkillSerializer, HomeServiceSerializer, HomeProcessSerializer, HomeToolSerializer, HomeFAQSerializer, HomeCTASerializer

class HomeHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeHero.objects.filter(is_active=True)
    serializer_class = HomeHeroSerializer
    ordering = ['created_at']

class HomeStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeStat.objects.filter(is_active=True)
    serializer_class = HomeStatSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'name']
    ordering = ['order']

class HomeIntroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeIntro.objects.filter(is_active=True)
    serializer_class = HomeIntroSerializer
    ordering = ['created_at']

class HomeSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeSkill.objects.filter(is_active=True)
    serializer_class = HomeSkillSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']

class HomeServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeService.objects.filter(is_active=True)
    serializer_class = HomeServiceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']

class HomeProcessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeProcess.objects.filter(is_active=True)
    serializer_class = HomeProcessSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']

class HomeToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeTool.objects.filter(is_active=True)
    serializer_class = HomeToolSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']

class HomeFAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeFAQ.objects.filter(is_active=True)
    serializer_class = HomeFAQSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'question']
    ordering = ['order']

class HomeCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeCTA.objects.filter(is_active=True)
    serializer_class = HomeCTASerializer
    ordering = ['created_at']