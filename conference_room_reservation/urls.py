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
from django.urls import re_path, path

from conference_rooms.views import (
    HomepageView,
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
    re_path(r'^$', HomepageView.as_view(), name='homepage-view'),
    re_path(r'^rooms/$', RoomsListView.as_view(), name='rooms-list-view'),
    re_path(r'^room/(?P<id>(\d)+)/$', RoomDetailView.as_view(), name='room-detail-view'),
    re_path(r'^room/new/$', RoomCreateView.as_view(), name='room-create-view'),
    re_path(r'^room/modify/(?P<id>(\d)+)/$', RoomUpdateView.as_view(), name='room-update-view'),
    re_path(r'^room/delete/(?P<id>(\d)+)/$', RoomDeleteView.as_view(), name='room-delete-view'),
    re_path(r'^reservations/$', ReservationsListView.as_view(), name='reservations-list-view'),
    re_path(r'^reservation/(?P<id>(\d)+)/$', ReservationDetailView.as_view(), name='reservation-detail-view'),
    re_path(r'^reservation/new/$', ReservationCreateView.as_view(), name='reservation-create-view'),
    re_path(r'^reservation/modify/(?P<id>(\d)+)/$', ReservationUpdateView.as_view(), name='reservation-update-view'),
    re_path(r'^reservation/delete/(?P<id>(\d)+)/$', ReservationDeleteView.as_view(), name='reservation-delete-view'),
]
