# about/tests.py (Updated)

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import AboutHero, Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent

class AboutApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.hero = AboutHero.objects.create(
            title="Turning Moments Into Timeless Art",
            subtitle="I'm Alex Rodriguez, a passionate videographer...",
            video="test.mp4",
            button_text="Watch My Story",
            is_active=True
        )
        self.stat = Stat.objects.create(name="Projects", value=500, suffix="+", icon="Briefcase", order=1, is_active=True)
        self.core_value = CoreValue.objects.create(
            title="Passion-Driven",
            description="Every project is approached with genuine enthusiasm",
            icon="Heart",
            order=1,
            is_active=True
        )
        self.timeline_event = TimelineEvent.objects.create(
            year="2016",
            title="The Beginning",
            description="Started freelance videography",
            icon="PlayCircle",
            order=1,
            is_active=True
        )
        self.skill = Skill.objects.create(
            name="Cinematography",
            level=95,
            icon="Camera",
            order=1,
            is_active=True
        )
        self.cta = AboutCTA.objects.create(
            title="Let's Create Together",
            description="Ready to turn your vision into a cinematic masterpiece?",
            button_text="Get In Touch",
            is_active=True
        )
        self.tab_content = AboutTabContent.objects.create(
            tab_name="story",
            title="My Journey",
            content="Paragraph 1\nParagraph 2\nParagraph 3",
            is_active=True
        )

    def test_about_hero_list(self):
        response = self.client.get('/about/hero/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Turning Moments Into Timeless Art")

    def test_stat_list(self):
        response = self.client.get('/about/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Projects")

    def test_core_value_list(self):
        response = self.client.get('/about/core-values/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Passion-Driven")

    def test_timeline_event_list(self):
        response = self.client.get('/about/timeline/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['year'], "2016")

    def test_skill_list(self):
        response = self.client.get('/about/skills/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Cinematography")

    def test_cta_list(self):
        response = self.client.get('/about/cta/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Let's Create Together")

    def test_tab_content_list(self):
        response = self.client.get('/about/tab-content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tab_name'], "story")

    def tearDown(self):
        self.hero.delete()
        self.stat.delete()
        self.core_value.delete()
        self.timeline_event.delete()
        self.skill.delete()
        self.cta.delete()
        self.tab_content.delete()