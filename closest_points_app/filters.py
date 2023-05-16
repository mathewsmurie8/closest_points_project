"""closest_points_app filters."""

import django_filters
from .models import PointSet

class PointSetFilter(django_filters.FilterSet):
    import pdb
    pdb.set_trace()
    class Meta:
        model = PointSet
        fields = ('id', 'received_points', 'closest_points')
