from django.db import models
from datetime import datetime

# python manage.py makemigrations 
# python manage.py migrate
# Create your models here.

class SourceText(models.Model):
    """ Таблица исходных текстов файлов (подчиненная  FileName ), """

    structure_txt = models.TextField('Исходный текст', blank=True)

    def __str__(self):
        return self.structure_txt

class FileName(models.Model):
    """ Таблица файлов, дата загрузки и признак анализа"""

    source_oto = models.ForeignKey(SourceText, on_delete=models.SET_NULL, null=True)

    file_name_chr = models.CharField('Имя файла', max_length=150)
    add_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    analize_bool = models.BooleanField('Анализ', default=False, blank=True)

    def __str__(self):
        return self.file_name_chr





