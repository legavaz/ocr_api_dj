from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, permissions, viewsets
from .models import FileName, SourceText
from .serializers import (
    FileNameListSerializer,
    FileNameDetailSerializer,
    SourceTextCreateSerializer,
    FileNameCreateSerializer,
)


def analiz_func(name_vol, volume):
    print(name_vol, volume, type(volume))



class FileNameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка файлов"""

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
        analiz_func('request.data', request.data)

        file_dic = {"file_name_chr": request.data.get("file")}
        source_dic = {"structure_txt": request.data.get("source")}

        source_set = SourceTextCreateSerializer(data=source_dic)

        if source_set.is_valid():
            source_obj = source_set.save()

            # Запрос - Исходный текст
            # file_dic = request.data.get("file")
            file_dic.update({'source_oto': source_obj.id})
            # analiz_func('file_dic', file_dic)

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
