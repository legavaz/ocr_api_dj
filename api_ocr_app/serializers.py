from rest_framework import serializers
from .models import FileName, SourceText


class FileNameListSerializer(serializers.ModelSerializer):
    """Вывод полного списка файлов"""

    class Meta:
        model = FileName
        fields = '__all__'


class FileNameDetailSerializer(serializers.ModelSerializer):
    """Вывод детальной информации файла"""
    source_oto = serializers.SlugRelatedField(slug_field="structure_txt", read_only=True)

    class Meta:
        model = FileName
        fields = '__all__'


class SourceTextCreateSerializer(serializers.ModelSerializer):
    """Добавление новой записи таблицы (SourceText)"""

    class Meta:
        model = SourceText
        fields = ("structure_txt",)


class FileNameCreateSerializer(serializers.ModelSerializer):
    """Добавление новой записи таблицы (файлы)"""

    # source_oto = SourceTextCreateSerializer(source="SourceText")

    # source_oto = SourceTextCreateSerializer()

    class Meta:
        model = FileName
        fields = "__all__"

    def create(self, validated_data):
        print('def create: validated_data', validated_data)
        # file_set = FileName.objects.update_or_create(
        file_set = FileName.objects.create(
            file_name_chr=validated_data.get('file_name_chr', None),
            file_name_short_chr=validated_data.get('file_name_short_chr', None),
            source_oto=validated_data.get('source_oto', None)
        )
        print('validated_data.get', validated_data.get('source_oto', None), type(validated_data.get('source_oto', None)))
        print('file_set', file_set, type(file_set))
        print('file_set.id', file_set.id, type(file_set.id))
        return file_set


