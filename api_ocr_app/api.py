from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import FileName, SourceText
from .serializers import (
    FileNameListSerializer,
    SourceListTextSerializer,
)


class FileNameViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = FileName.objects.all()
        serializer = FileNameListSerializer(queryset, many=True)
        return Response(serializer.data)
