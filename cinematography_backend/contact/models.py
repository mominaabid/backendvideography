# contact/models.py

from django.db import models
from django.core.validators import FileExtensionValidator


class ContactInfo(models.Model):
    ICON_CHOICES = [
        ('Phone', 'Phone'),
        ('Mail', 'Mail'),
        ('MapPin', 'MapPin'),
        ('Clock', 'Clock'),
    ]
    
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'
    
    def __str__(self):
        return f"{self.title} - {self.info}"


class WhyChooseUs(models.Model):
    ICON_CHOICES = [
        ('Award', 'Award'),
        ('Star', 'Star'),
        ('Heart', 'Heart'),
        ('Camera', 'Camera'),
        ('Users', 'Users'),
        ('TrendingUp', 'TrendingUp'),
    ]
    
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'
    
    def __str__(self):
        return self.title


class HeroSection(models.Model):
    PAGE_CHOICES = [
        ('contact', 'Contact Page'),
        ('services', 'Services Page'),
        ('home', 'Home Page'),
        ('about', 'About Page'),
    ]
    
    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('image', 'Image'),
    ]
    
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = models.TextField(blank=True, help_text='Additional description text')
    badge_text = models.CharField(max_length=100, blank=True)
    badge_icon = models.CharField(max_length=50, blank=True, help_text='Icon name (e.g., MessageSquare, Award)')
    
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='video')
    video = models.FileField(
        upload_to='hero_videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov'])],
        blank=True,
        null=True,
        help_text='Upload hero video (MP4, WebM, or MOV format)'
    )
    image = models.ImageField(
        upload_to='hero_images/',
        blank=True,
        null=True,
        help_text='Upload hero image (JPG, PNG, WebP format)'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'
    
    def __str__(self):
        return f"Hero Section - {self.get_page_display()}"
    
    def get_media_url(self):
        if self.media_type == 'video' and self.video:
            return self.video.url
        elif self.media_type == 'image' and self.image:
            return self.image.url
        return None


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, help_text='Internal notes (not visible to user)')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"