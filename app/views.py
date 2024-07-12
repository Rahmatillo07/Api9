from django.shortcuts import render

from .models import Video
from .serializers import VideoSerializer

from rest_framework.viewsets import ModelViewSet


class VideoApiView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
