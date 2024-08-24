from django.contrib import admin
from .models import HotelRoom, UserQuery


# Register the HotelRoom model
@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'is_available', 'price')  # Ensure these fields exist in your model
    search_fields = ('room_number',)  # Add fields you want to search by


# Register the UserQuery model
@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'user', 'created_at')  # Ensure these fields exist in your model
    search_fields = ('query', 'user')  # Add fields you want to search by
