# portfolio/serializers.py

from rest_framework import serializers
from .models import PortfolioCategory, HeroSlide, Project


# ---------------- Hero Slide ----------------
class HeroSlideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSlide
        fields = [
            'id', 'image', 'image_url', 'video', 'video_url',
            'title', 'category', 'views', 'order', 'is_active',
            'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        """Return Cloudinary image URL"""
        try:
            if obj.image:
                return obj.image.url
        except:
            return None
        return None

    def get_video_url(self, obj):
        """Return Cloudinary video URL"""
        try:
            if obj.video:
                return obj.video.url
        except:
            return None
        return None


# ---------------- Project ----------------
class ProjectSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'category', 'thumbnail', 'thumbnail_url',
            'video', 'video_url', 'image', 'image_url',
            'description', 'views', 'likes', 'order',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_video_url(self, obj):
        """Return Cloudinary video URL"""
        try:
            if obj.video:
                return obj.video.url
        except:
            return None
        return None

    def get_image_url(self, obj):
        """Return Cloudinary image URL"""
        try:
            if obj.image:
                return obj.image.url
        except:
            return None
        return None

    def get_thumbnail_url(self, obj):
        """Return Cloudinary thumbnail URL"""
        try:
            if obj.thumbnail:
                return obj.thumbnail.url
        except:
            return None
        return None


# ---------------- Portfolio Category ----------------
class PortfolioCategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioCategory
        fields = [
            'id', 'name', 'icon', 'count',
            'projects', 'order', 'is_active'
        ]
