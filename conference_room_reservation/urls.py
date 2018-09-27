"""conference_room_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homeapp.views import HomepageView
from conference_rooms.views import (
    RoomsListView,
    RoomDetailView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
    ReservationsListView,
    ReservationDetailView,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage-view'),
    path('rooms/', RoomsListView.as_view(), name='rooms-list-view'),
    path('room/<int:id>/', RoomDetailView.as_view(), name='room-detail-view'),
    path('room/new/', RoomCreateView.as_view(), name='room-create-view'),
    path('room/modify/<int:id>/', RoomUpdateView.as_view(), name='room-update-view'),
    path('room/delete/<int:id>/', RoomDeleteView.as_view(), name='room-delete-view'),
    path('reservations/', ReservationsListView.as_view(), name='reservations-list-view'),
    path('reservation/<int:id>/', ReservationDetailView.as_view(), name='reservation-detail-view'),
    path('reservation/new/', ReservationCreateView.as_view(), name='reservation-create-view'),
    path('reservation/modify/<int:id>/', ReservationUpdateView.as_view(), name='reservation-update-view'),
    path('reservation/delete/<int:id>/', ReservationDeleteView.as_view(), name='reservation-delete-view'),
]
