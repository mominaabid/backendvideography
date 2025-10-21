# portfolio/models.py

from django.db import models
from django.core.validators import FileExtensionValidator

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, help_text='e.g., Wedding, Real Estate')
    icon = models.CharField(max_length=50, choices=[
        ('Sparkles', 'Sparkles'),  # For All Projects
        ('Heart', 'Heart'),        # For Weddings
        ('Building2', 'Building2'), # For Real Estate
        ('MessageCircle', 'MessageCircle'), # For Talking Head
        ('Film', 'Film'),          # For Commercial
    ], default='Sparkles')
    count = models.IntegerField(default=0, help_text='Number of projects in this category')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    is_active = models.BooleanField(default=True, help_text='Display this category on the website')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Portfolio Categories'

    def __str__(self):
        return self.name


class HeroSlide(models.Model):
    image = models.ImageField(upload_to='hero_slides/', help_text='Upload hero slide image')
    video = models.FileField(
        upload_to='hero_videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov'])],
        help_text='Upload hero slide video (MP4, WebM, or MOV format)'
    )
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.CharField(max_length=10, default='0', help_text='e.g., 25K')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    is_active = models.BooleanField(default=True, help_text='Display this slide on the website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Hero Slide'
        verbose_name_plural = 'Hero Slides'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='projects')
    thumbnail = models.ImageField(upload_to='project_thumbnails/', help_text='Upload project thumbnail image')
    video = models.FileField(
        upload_to='project_videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov'])],
        help_text='Upload project video (MP4, WebM, or MOV format)'
    )
    description = models.TextField(help_text='Project description')
    views = models.CharField(max_length=10, default='0', help_text='e.g., 12.5K')
    likes = models.CharField(max_length=10, default='0', help_text='e.g., 2.1K')
    order = models.IntegerField(default=0, help_text='Display order (lower numbers appear first)')
    is_active = models.BooleanField(default=True, help_text='Display this project on the website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
