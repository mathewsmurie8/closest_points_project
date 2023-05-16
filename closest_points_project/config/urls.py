from django.urls import path, include

urlpatterns = [
    path('', include('closest_points_project.closest_points_app.urls')),
]
