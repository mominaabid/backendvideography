# home/serializers.py

from rest_framework import serializers
from .models import HomeHero, HomeStat, HomeIntro, HomeSkill, HomeService, HomeProcess, HomeTool, HomeFAQ, HomeCTA

class HomeHeroSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    typewriter_phrases = serializers.SerializerMethodField()

    class Meta:
        model = HomeHero
        fields = ['id', 'title', 'typewriter_phrases', 'subtitle', 'video', 'video_url', 'primary_button_text', 'secondary_button_text', 'is_active', 'created_at', 'updated_at']

    def get_video_url(self, obj):
        if obj.video:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video.url)
        return None

    def get_typewriter_phrases(self, obj):
        return obj.typewriter_phrases.split(',')

class HomeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStat
        fields = ['id', 'name', 'value', 'suffix', 'icon', 'order', 'is_active']

class HomeIntroSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()

    class Meta:
        model = HomeIntro
        fields = ['id', 'title', 'subtitle', 'image', 'image_url', 'achievements', 'primary_button_text', 'secondary_button_text', 'is_active', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None

    def get_achievements(self, obj):
        return obj.achievements.split(',')

class HomeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSkill
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']

class HomeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeService
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']

class HomeProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProcess
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']

class HomeToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTool
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']

class HomeFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFAQ
        fields = ['id', 'question', 'answer', 'order', 'is_active']

class HomeCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCTA
        fields = ['id', 'title', 'description', 'button_text', 'is_active', 'created_at', 'updated_at']