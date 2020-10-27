from .models import Source_table
from rest_framework import viewsets, permissions
from .serializers import Source_tableSerializer


# Source_table ViewSet
class Source_tableViewSet(viewsets.ModelViewSet):
    queryset = Source_table.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Source_tableSerializer