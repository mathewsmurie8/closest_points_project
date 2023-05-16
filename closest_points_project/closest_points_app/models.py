import uuid
from django.db import models
from django.utils import timezone

class PointSet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(db_index=True, default=timezone.now)
    received_points = models.TextField()
    closest_points = models.TextField(null=True, blank=True)
