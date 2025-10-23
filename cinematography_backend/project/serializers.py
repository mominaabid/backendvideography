# cinematography_backend/project/serializers.py

from rest_framework import serializers
from .models import PortfolioHero, Project

class PortfolioHeroSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()
    
    class Meta:
        model = PortfolioHero
        fields = [
            'id',
            'title',
            'subtitle',
            'button_text',
          
            'media_type',
            'media_url',
            'is_active',
            'created_at',
            'updated_at'
        ]
    
    def get_media_url(self, obj):
        request = self.context.get('request')
        media_url = obj.get_media_url()
        if media_url and request:
            return request.build_absolute_uri(media_url)
        return media_url


class ProjectListSerializer(serializers.ModelSerializer):
    """Serializer for project list view"""
    media_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'media_type',
            'media_url',
            'thumbnail_url',
            'client',
            'technologies_list',
            'is_featured',
            'created_at'
        ]
    
    def get_media_url(self, obj):
        request = self.context.get('request')
        media_url = obj.get_media_url()
        if media_url and request:
            return request.build_absolute_uri(media_url)
        return media_url
    
    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        thumbnail_url = obj.get_thumbnail_url()
        if thumbnail_url and request:
            return request.build_absolute_uri(thumbnail_url)
        return thumbnail_url
    
    def get_technologies_list(self, obj):
        if obj.technologies:
            return [tech.strip() for tech in obj.technologies.split(',')]
        return []


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serializer for project detail view"""
    media_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'details',
            'media_type',
            'media_url',
            'thumbnail_url',
            'client',
            'project_url',
            'technologies_list',
            'is_featured',
            'created_at',
            'updated_at'
        ]
    
    def get_media_url(self, obj):
        request = self.context.get('request')
        media_url = obj.get_media_url()
        if media_url and request:
            return request.build_absolute_uri(media_url)
        return media_url
    
    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        thumbnail_url = obj.get_thumbnail_url()
        if thumbnail_url and request:
            return request.build_absolute_uri(thumbnail_url)
        return thumbnail_url
    
    def get_technologies_list(self, obj):
        if obj.technologies:
            return [tech.strip() for tech in obj.technologies.split(',')]
        return []