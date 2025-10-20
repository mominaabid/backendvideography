# services/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, ProcessStepViewSet,
    EquipmentCategoryViewSet, TestimonialViewSet,
    site_stats_view
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'process-steps', ProcessStepViewSet, basename='processstep')
router.register(r'equipment', EquipmentCategoryViewSet, basename='equipment')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', site_stats_view, name='site-stats'),
]