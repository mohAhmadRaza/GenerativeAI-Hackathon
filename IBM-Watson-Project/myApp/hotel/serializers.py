# hotel/serializers.py
from rest_framework import serializers
from .models import UserQuery, HotelRoom


class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        fields = ['id', 'query', 'user', 'created_at']


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ['id', 'room_number', 'is_available']
