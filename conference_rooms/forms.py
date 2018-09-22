from django import forms
from .models import Room, Reservation


class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'capacity',
            'projector_is_available',
            'is_active',
        ]


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'room',
            'date',
            'comment',
        ]
