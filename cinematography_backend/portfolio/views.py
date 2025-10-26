# portfolio/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import PortfolioCategory, HeroSlide, Project
from .serializers import PortfolioCategorySerializer, HeroSlideSerializer, ProjectSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MediaFile

class UploadMediaView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.data.get('file')
        title = request.data.get('title', 'Untitled')

        if not file:
            return Response({"error": "No file provided."}, status=400)

        media = MediaFile.objects.create(title=title, file=file)
        return Response({
            "id": media.id,
            "title": media.title,
            "file_url": media.file.url,
        })


class PortfolioCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PortfolioCategory.objects.filter(is_active=True).prefetch_related('projects')
    serializer_class = PortfolioCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['order', 'name']
    search_fields = ['name']
    ordering = ['order']


class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSlide.objects.filter(is_active=True)
    serializer_class = HeroSlideSerializer
    ordering = ['order']


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering = ['order']