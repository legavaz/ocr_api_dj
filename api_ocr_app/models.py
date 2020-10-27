from django.db import models

# python manage.py makemigrations 
# python manage.py migrate
# Create your models here.

class Source_table(models.Model):
    file_name_chr = models.CharField(max_length=150)
    add_date = models.DateTimeField(auto_now_add=True)
    analize_date = models.DateTimeField(null=True,blank=True)
    analize_bool = models.BooleanField(default=False,blank=True)
    structure_txt = models.TextField(blank=True)

    def __str__(self):
        return self.file_name_chr