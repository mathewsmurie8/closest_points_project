from django.urls import path
from .views import ClosestPointsView, PointSetListView

urlpatterns = [
    path('', PointSetListView.as_view()),
    path('pointsets/', PointSetListView.as_view()),
    path('closest-points/', ClosestPointsView.as_view()),
]
