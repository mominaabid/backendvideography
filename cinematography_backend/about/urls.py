from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutHeroViewSet, StatViewSet, CoreValueViewSet, TimelineEventViewSet, SkillViewSet, AboutCTAViewSet, AboutTabContentViewSet

router = DefaultRouter()
router.register(r'hero', AboutHeroViewSet, basename='about_hero')
router.register(r'stats', StatViewSet, basename='stat')
router.register(r'core-values', CoreValueViewSet, basename='core_value')
router.register(r'timeline', TimelineEventViewSet, basename='timeline_event')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'cta', AboutCTAViewSet, basename='about_cta')
router.register(r'tab-content', AboutTabContentViewSet, basename='tab_content')

urlpatterns = [
    path('', include(router.urls)),
]