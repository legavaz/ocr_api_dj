from django.contrib import admin
from .models import FileName, SourceText


@admin.register(FileName)
class FileNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name_chr', 'add_date', 'source_oto', 'analize_bool')
    list_display_links = ('id', 'file_name_chr')
    list_filter = ('analize_bool',)

    search_fields = ('id', 'file_name_chr')


@admin.register(SourceText)
class SourceTextAdmin(admin.ModelAdmin):
    """Рейтинг фильма"""
    list_display = ('id', 'add_date', 'structure_txt')
