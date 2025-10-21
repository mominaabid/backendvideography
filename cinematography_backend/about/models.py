# about/models.py (Updated)

from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

class AboutHero(models.Model):
    title = models.CharField(max_length=200, help_text="Main title for the hero section (e.g., 'Turning Moments Into Timeless Art')")
    subtitle = models.TextField(help_text="Subtitle or description for the hero section")
    video = models.FileField(
        upload_to='about_hero_videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov'])],
        help_text="Upload hero section video (MP4, WebM, or MOV format)"
    )
    button_text = models.CharField(max_length=100, default="Watch My Story", help_text="Text for the hero section button")
    is_active = models.BooleanField(default=True, help_text="Display this hero content on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Hero"
        verbose_name_plural = "About Hero Sections"

    def __str__(self):
        return self.title

class Stat(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Projects, Happy Clients")
    value = models.IntegerField(default=0, help_text="Numeric value for the stat (e.g., 500)")
    suffix = models.CharField(max_length=10, default="+", help_text="Suffix for the stat (e.g., '+')")
    icon = models.CharField(max_length=50, choices=[
        ('Briefcase', 'Briefcase'),
        ('Users', 'Users'),
        ('Award', 'Award'),
        ('Globe', 'Globe'),
    ], default='Briefcase')
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this stat on the website")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.name} - {self.value}{self.suffix}"

class CoreValue(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., Passion-Driven")
    description = models.TextField(help_text="Description of the core value")
    icon = models.CharField(max_length=50, choices=[
        ('Heart', 'Heart'),
        ('Eye', 'Eye'),
        ('Lightbulb', 'Lightbulb'),
        ('Users', 'Users'),
    ], default='Heart')
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this core value on the website")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title

class TimelineEvent(models.Model):
    year = models.CharField(max_length=4, help_text="e.g., 2016")
    title = models.CharField(max_length=100, help_text="e.g., The Beginning")
    description = models.TextField(help_text="Description of the timeline event")
    icon = models.CharField(max_length=50, choices=[
        ('PlayCircle', 'PlayCircle'),
        ('Award', 'Award'),
        ('Briefcase', 'Briefcase'),
        ('Globe', 'Globe'),
        ('Sparkles', 'Sparkles'),
    ], default='PlayCircle')
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this event on the website")

    class Meta:
        ordering = ['order', 'year']
        verbose_name = "Timeline Event"
        verbose_name_plural = "Timeline Events"

    def __str__(self):
        return f"{self.year} - {self.title}"

class Skill(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Cinematography")
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill level as a percentage (0-100)"
    )
    icon = models.CharField(max_length=50, choices=[
        ('Camera', 'Camera'),
        ('Sparkles', 'Sparkles'),
        ('Film', 'Film'),
        ('Zap', 'Zap'),
        ('Target', 'Target'),
        ('Eye', 'Eye'),
    ], default='Camera')
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Display this skill on the website")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} - {self.level}%"

class AboutCTA(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Let's Create Together")
    description = models.TextField(help_text="Description for the CTA section")
    button_text = models.CharField(max_length=100, default="Get In Touch", help_text="Text for the CTA button")
    is_active = models.BooleanField(default=True, help_text="Display this CTA on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About CTA"
        verbose_name_plural = "About CTAs"

    def __str__(self):
        return self.title

# about/models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class AboutTabContent(models.Model):
    tab_name = models.CharField(
        max_length=50,
        choices=[
            ('story', 'Story'),
            ('philosophy', 'Philosophy'),
            ('approach', 'Approach'),
        ],
        unique=True,
        help_text="Name of the tab (Story, Philosophy, or Approach)"
    )
    title = models.CharField(max_length=100, help_text="e.g., My Journey")
    content = models.TextField(help_text="Content for the tab, supports multiple paragraphs separated by newlines")
    image = models.ImageField(  # New image field
        upload_to='about_tab_images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        help_text="Image for the tab (JPG, JPEG, or PNG format)",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True, help_text="Display this tab content on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Tab Content"
        verbose_name_plural = "About Tab Contents"

    def __str__(self):
        return f"{self.tab_name} - {self.title}"