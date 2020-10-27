from rest_framework import serializers
from .models import Source_table


# Todo serializer
class Source_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source_table
        fields = '__all__'