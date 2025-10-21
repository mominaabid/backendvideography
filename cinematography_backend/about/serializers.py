# about/serializers.py (Updated)

from rest_framework import serializers
from .models import AboutHero, Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent

class AboutHeroSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutHero
        fields = ['id', 'title', 'subtitle', 'video', 'video_url', 'button_text', 'is_active', 'created_at', 'updated_at']

    def get_video_url(self, obj):
        if obj.video:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video.url)
        return None

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'name', 'value', 'suffix', 'icon', 'order', 'is_active']

class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = ['id', 'title', 'description', 'icon', 'order', 'is_active']

class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = ['id', 'year', 'title', 'description', 'icon', 'order', 'is_active']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level', 'icon', 'order', 'is_active']

class AboutCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCTA
        fields = ['id', 'title', 'description', 'button_text', 'is_active', 'created_at', 'updated_at']

class AboutTabContentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Include image URL

    class Meta:
        model = AboutTabContent
        fields = ['id', 'tab_name', 'title', 'content', 'image', 'is_active', 'created_at', 'updated_at']