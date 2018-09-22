from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)

from .models import (
    Room,
    Reservation,
)

from .forms import (
    ReservationCreateForm,
    RoomCreateForm,
)


class RoomDetailView(DetailView):
    template_name = 'conference_rooms/room-detail-view.html'
    queryset = Room.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)


class RoomCreateView(CreateView):
    template_name = 'conference_rooms/room-create-view.html'
    form_class = RoomCreateForm


class RoomUpdateView(UpdateView):
    template_name = 'conference_rooms/room-create-view.html'
    form_class = RoomCreateForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')


class ReservationDetailView(DetailView):
    template_name = 'conference_rooms/reservation-detail-view.html'
    queryset = Reservation.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id_)


class ReservationCreateView(CreateView):
    template_name = 'conference_rooms/reservation-create-view.html'
    form_class = ReservationCreateForm


class ReservationUpdateView(UpdateView):
    template_name = 'conference_rooms/reservation-create-view.html'
    form_class = ReservationCreateForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id_)
