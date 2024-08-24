# hotel/urls.py
from django.urls import path
from .views import UserQueryView, HotelRoomsAvailabilityView, BookHotelRoomView

urlpatterns = [
    path('userQuery/', UserQueryView.as_view(), name='user_query'),
    path('hotelRoomsAvailability/', HotelRoomsAvailabilityView.as_view(), name='hotel_rooms_availability'),
    path('bookHotelRoom/', BookHotelRoomView.as_view(), name='book_hotel_room'),
]
