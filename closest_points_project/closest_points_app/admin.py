from django.contrib import admin
from .models import PointSet
from import_export.admin import ImportExportModelAdmin


class PointSetAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'received_points', 'closest_points', 'created')
    list_display_links = ('id', 'received_points', 'closest_points', 'created')
    search_fields = ('id', 'received_points', 'closest_points', 'created')
    list_per_page = 25

admin.site.register(PointSet, PointSetAdmin)
