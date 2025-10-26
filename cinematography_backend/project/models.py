from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField  # ✅ Add this import


# ---------------- Media Uploads ----------------
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('file', blank=True, null=True)  # ✅ Cloudinary instead of FileField
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- Portfolio Hero Section ----------------
class PortfolioHero(models.Model):
    """Model for the portfolio hero section"""
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100, default="Start Your Project")

    # Media field - can be image or video
    media_type = models.CharField(
        max_length=10,
        choices=[('image', 'Image'), ('video', 'Video')],
        default='image'
    )

    image = CloudinaryField('image', blank=True, null=True)  # ✅ CloudinaryField replaces ImageField
    video = CloudinaryField('video', blank=True, null=True)  # ✅ CloudinaryField replaces FileField

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'portfolio_hero'
        verbose_name = 'Portfolio Hero Section'
        verbose_name_plural = 'Portfolio Hero Sections'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_media_url(self):
        """Returns the URL of the active media (image or video)"""
        if self.media_type == 'image' and self.image:
            return self.image.url
        elif self.media_type == 'video' and self.video:
            return self.video.url
        return None


# ---------------- Projects ----------------
class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField()

    # Media field - can be image or video
    media_type = models.CharField(
        max_length=10,
        choices=[('image', 'Image'), ('video', 'Video')],
        default='image'
    )

    image = CloudinaryField('image', blank=True, null=True)     # ✅ Cloudinary
    video = CloudinaryField('video', blank=True, null=True)     # ✅ Cloudinary
    thumbnail = CloudinaryField('image', blank=True, null=True) # ✅ Cloudinary thumbnail

    # Additional fields
    client = models.CharField(max_length=200, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=500, blank=True, null=True, help_text="Comma-separated technologies")

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Order of display (lower numbers first)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_media_url(self):
        """Returns the URL of the active media (image or video)"""
        if self.media_type == 'image' and self.image:
            return self.image.url
        elif self.media_type == 'video' and self.video:
            return self.video.url
        return None

    def get_thumbnail_url(self):
        """Returns thumbnail URL, preferring custom thumbnail for videos"""
        if self.media_type == 'video' and self.thumbnail:
            return self.thumbnail.url
        elif self.media_type == 'image' and self.image:
            return self.image.url
        return None
