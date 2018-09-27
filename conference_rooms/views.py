import datetime
from django.shortcuts import  get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import (
    Room,
    Reservation,
)

from .forms import (
    ReservationCreateForm,
    RoomCreateForm,
)


class RoomsListView(ListView):
    template_name = 'conference_rooms/rooms-list-view.html'
    queryset = Room.objects.all().order_by('id')


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
        return get_object_or_404(Room, id=id_)


class RoomDeleteView(DeleteView):
    template_name = 'conference_rooms/room-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_success_url(self):
        return reverse('rooms-list-view')


class ReservationsListView(ListView):
    template_name = 'conference_rooms/reservations-list-view.html'
    queryset = Reservation.objects.all().order_by('-date')
    # queryset = Reservation.objects.filter(date__gte=datetime.datetime.now())


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


class ReservationDeleteView(DeleteView):
    template_name = 'conference_rooms/reservation-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id_)

    def get_success_url(self):
        return reverse('reservations-list-view')
