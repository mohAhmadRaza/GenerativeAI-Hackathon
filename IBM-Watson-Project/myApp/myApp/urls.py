from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotel.urls')),  # Include the URLs from the hotel app
]

