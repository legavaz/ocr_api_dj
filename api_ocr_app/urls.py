from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("files/", views.FileNameViewSet.as_view({'get': 'list'})),
    path("files/<int:pk>/", views.FileNameViewSet.as_view({'get': 'retrieve'})),
    path("file_add/", views.FileCreateViewSet.as_view()),

    # # для отладки
    # path("source_add/", views.SourceTextCreateViewSet.as_view()),
])
