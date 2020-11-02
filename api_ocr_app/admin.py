from django.contrib import admin
from .models import Source_table


class Source_table_admin(admin.ModelAdmin):
    list_display = ('id', 'file_name_chr','add_date', 'structure_txt', 'analize_bool')
    list_display_links = ('id', 'file_name_chr')
    list_filter = ('analize_bool',)
    
    search_fields = ('id', 'file_name_chr', 'structure_txt')

admin.site.register(Source_table,Source_table_admin)