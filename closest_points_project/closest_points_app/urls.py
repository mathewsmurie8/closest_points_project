from django.contrib import admin
from django.urls import path
from .views import ClosestPointsView, PointSetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PointSetListView.as_view()),
    path('pointsets/', PointSetListView.as_view()),
    path('closest-points/', ClosestPointsView.as_view()),
]
