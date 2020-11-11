from django_filters import rest_framework as filters
from .models import FileName


class FileNameFilter(filters.FilterSet):
    file_name = filters.CharFilter(field_name='file_name_short_chr')

    class Meta:
        model = FileName
        fields = ['file_name']
