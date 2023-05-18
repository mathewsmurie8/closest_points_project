"""closest_points_app filters."""

import django_filters
from .models import PointSet

class PointSetFilter(django_filters.FilterSet):
    class Meta:
        model = PointSet
        fields = ('id', 'received_points', 'closest_points')
