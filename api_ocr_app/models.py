from django.db import models
from datetime import datetime,timezone

# python manage.py makemigrations 
# python manage.py migrate
# Create your models here.

class SourceText(models.Model):
    """ Таблица исходных текстов файлов (подчиненная  FileName ), """

    structure_txt = models.TextField('Исходный текст', blank=True)
    add_date = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.structure_txt

class Customers(models.Model):
    """ Таблица контрагентов
     -поля (Имя, ИНН, КПП)
     """
    name = models.CharField('Наименование', max_length=100)
    inn = models.CharField('Наименование', max_length=50)
    kpp = models.CharField('Наименование', max_length=9, blank=True)
    guid = models.CharField('Идентификатор', max_length=60)


class Nomenklatura(models.Model):
    """ Таблица Номенклатура
     -поля (Имя, ИНН, КПП)
     """
    name = models.CharField('Наименование', max_length=150)
    guid = models.CharField('Идентификатор', max_length=60)


class FileName(models.Model):
    """ Таблица файлов, дата загрузки и признак анализа"""

    source_oto = models.ForeignKey(SourceText, on_delete=models.SET_NULL, null=True)

    file_name_chr = models.CharField('Имя файла (полное)', max_length=150)
    file_name_short_chr = models.CharField('Имя файла (короткое)', max_length=150, blank=True,null=True)
    add_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    analize_bool = models.BooleanField('Анализ', default=False, blank=True)

    def __str__(self):
        return self.file_name_chr





