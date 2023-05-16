from rest_framework import serializers
from .models import PointSet

class PointSetSerializer(serializers.ModelSerializer):
    """PointSet serializer."""

    class Meta:
        model = PointSet
        fields = '__all__'
