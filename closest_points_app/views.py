from django.http import Http404
from rest_framework import filters, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PointSet
from .serializers import PointSetSerializer
from .utils import find_closest_points

class PointSetListView(ListAPIView):
    queryset = PointSet.objects.all()
    serializer_class = PointSetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'received_points', 'closest_points']

class ClosestPointsView(APIView):
    queryset = PointSet.objects.all()
    serializer_class = PointSetSerializer

    def post(self, request):
        try:
            points_str = request.data.get("received_points")
            if not points_str:
                return Response({"error": "'received_points' field is required."}, status=status.HTTP_400_BAD_REQUEST)
            points = [list(map(int, point.split(','))) for point in points_str.split(';')]
            if len(points) < 2:
                return Response({"error": "At least two points are required."}, status=status.HTTP_400_BAD_REQUEST)
            closest_points = find_closest_points(points)
            closest_points_str = ';'.join([','.join(map(str, point)) for point in closest_points])
            point_set = PointSet.objects.create(
                received_points=points_str,
                closest_points=closest_points_str,
            )
            point_set.save()
            return Response({"closest_points": closest_points_str})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
