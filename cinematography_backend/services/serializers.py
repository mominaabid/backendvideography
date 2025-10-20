# services/serializers.py

from rest_framework import serializers
from .models import (
    Service, ServiceFeature, ProcessStep,
    EquipmentCategory, EquipmentItem, Testimonial, SiteStats
)


class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ['id', 'feature_text', 'order']


class ServiceSerializer(serializers.ModelSerializer):
    features = ServiceFeatureSerializer(many=True, read_only=True)
    video_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = [
            'id', 'title', 'icon', 'video', 'video_url',
            'description', 'features', 'is_active', 
            'order', 'created_at', 'updated_at'
        ]
    
    def get_video_url(self, obj):
        if obj.video:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video.url)
        return None


class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = ['id', 'step_number', 'title', 'description', 'order', 'is_active']


class EquipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentItem
        fields = ['id', 'item_name', 'order']


class EquipmentCategorySerializer(serializers.ModelSerializer):
    items = EquipmentItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = EquipmentCategory
        fields = ['id', 'name', 'items', 'order']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'role', 'text', 'rating',
            'is_active', 'order', 'created_at'
        ]


class SiteStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStats
        fields = [
            'id', 'projects_completed', 'happy_clients',
            'industry_awards', 'client_satisfaction', 'updated_at'
        ]