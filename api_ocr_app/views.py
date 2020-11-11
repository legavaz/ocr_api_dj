from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import FileName, SourceText
from .serializers import (
    FileNameListSerializer,
    FileNameDetailSerializer,
    SourceTextCreateSerializer,
    FileNameCreateSerializer,
)
from .service import FileNameFilter

class FileNameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка файлов"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FileNameFilter

    def get_queryset(self):
        file_names = FileName.objects.filter()

        return file_names

    def get_serializer_class(self):
        if self.action == 'list':
            return FileNameListSerializer
        elif self.action == "retrieve":
             return FileNameDetailSerializer


class SourceTextCreateViewSet(APIView):
    """Добавление новой записи в таблицу файлы"""
    def post(self, request):
        _set = SourceTextCreateSerializer(data=request.data)
        if _set.is_valid():
            _set.save()
        return Response(status=201)


class FileCreateViewSet(APIView):
    """Добавление новой записи в таблицу файлы"""
    def post(self, request):
        m_result = False

        source_dic = {
            "structure_txt": request.data.get("source"),
                      }

        source_set = SourceTextCreateSerializer(data=source_dic)
        if source_set.is_valid():
            source_obj = source_set.save()

            file_dic = {
                "file_name_chr": request.data.get("file"),
                "file_name_short_chr": request.data.get("short"),
                'source_oto': source_obj.id
                }
            file_set = FileNameCreateSerializer(data=file_dic)

            if file_set.is_valid():
                file_set.save()
                m_result = True
            else:
                source_set.save()

        if m_result:
            return Response(status=201)
        else:
            return Response(status=400)
