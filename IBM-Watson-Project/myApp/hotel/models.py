# hotel/models.py
from django.db import models


class HotelRoom(models.Model):
    DoesNotExist = None
    objects = None
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)


class UserQuery(models.Model):
    query = models.CharField(max_length=255)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
