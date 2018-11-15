from datetime import datetime
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.urls import reverse_lazy

from django.views import View
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


class HomepageView(View):
    def get(self, request):
        return render(request, 'conference_rooms/base.html')


class RoomsListView(ListView):
    template_name = 'conference_rooms/rooms-list-view.html'
    queryset = Room.objects.all().order_by('id')


class RoomDetailView(DetailView):
    template_name = 'conference_rooms/room-detail-view.html'
    queryset = Room.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data()
        id_ = self.kwargs.get('id')
        context['reservations'] = Reservation.objects.filter(room_id=id_, date__gte=datetime.now()).order_by('date')
        return context


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
        return reverse_lazy('rooms-list-view')


class ReservationsListView(ListView):
    template_name = 'conference_rooms/reservations-list-view.html'
    queryset = Reservation.objects.filter(date__gte=datetime.now().date()).order_by('date')


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
        return reverse_lazy('reservations-list-view')
