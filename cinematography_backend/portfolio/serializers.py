# portfolio/serializers.py

from rest_framework import serializers
from .models import PortfolioCategory, HeroSlide, Project


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = ['id', 'image', 'video', 'title', 'category', 'views', 'order', 'is_active', 'created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'category', 'thumbnail', 'video', 'video_url', 'description', 'views', 'likes', 'order', 'is_active', 'created_at', 'updated_at']

    def get_video_url(self, obj):
        if obj.video:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video.url)
        return None


class PortfolioCategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioCategory
        fields = ['id', 'name', 'icon', 'count', 'projects', 'order', 'is_active']