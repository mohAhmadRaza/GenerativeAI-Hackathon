# hotel/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HotelRoom, UserQuery
from .serializers import HotelRoomSerializer, UserQuerySerializer


class UserQueryView(APIView):
    def get(self, request):
        queries = UserQuery.objects.all()
        serializer = UserQuerySerializer(queries, many=True)
        return Response(serializer.data)


class HotelRoomsAvailabilityView(APIView):
    def get(self, request):
        available_rooms = HotelRoom.objects.filter(is_available=True)
        serializer = HotelRoomSerializer(available_rooms, many=True)
        return Response(serializer.data)


class BookHotelRoomView(APIView):
    def post(self, request):
        room_id = request.data.get('room_id')
        try:
            room = HotelRoom.objects.get(id=room_id, is_available=True)
        except HotelRoom.DoesNotExist:
            return Response({"error": "Room not available"}, status=status.HTTP_400_BAD_REQUEST)

        room.is_available = False
        room.save()
        return Response({"message": "Room booked successfully!"}, status=status.HTTP_200_OK)
