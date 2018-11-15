from datetime import datetime

from django import forms
from django.core.validators import MinValueValidator
from django.db.models import Q

from .models import Room, Reservation

DATE_INPUT_FORMATS = (
    '%d/%m/%Y', '%Y/%m/%d',
    '%d-%m-%Y', '%Y-%m-%d',
    '%d.%m.%Y', '%Y.%m.%d',
    '%d,%m,%Y', '%Y,%m,%d',
    '%d %m %Y', '%Y %m %d',
)


class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'capacity',
            'projector_is_available',
            'is_active',
        ]


class RoomSearchForm(forms.Form):
    name = forms.CharField(label='Room Name', required=False)
    capacity = forms.IntegerField(label='Capacity', required=False, validators=[MinValueValidator(1)])
    projector = forms.BooleanField(label='Projector', required=False, initial=False,
                                   widget=forms.CheckboxInput())
    date = forms.DateField(label='Date', widget=forms.DateInput(format='%d/%m/%Y'), input_formats=DATE_INPUT_FORMATS)

    class Meta:
        fields = [
            'name',
            'capacity',
            'projector',
            'date',
        ]

    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= datetime.now().date():
            raise forms.ValidationError('Do not search date from the past')
        return date

    def search_room(self):
        date = self.cleaned_data['date']
        name = self.cleaned_data['name'] if self.cleaned_data['name'] else ''
        capacity = self.cleaned_data['capacity'] if self.cleaned_data['capacity'] else 1
        projector = self.cleaned_data['projector']

        queryset = Room.objects.filter(
            ~Q(reservation__date=date),
            Q(name__icontains=name),
            Q(capacity__gte=capacity),
            Q(projector_is_available=projector) if projector else Q(),
        )
        return queryset.distinct().order_by('-capacity')


class ReservationCreateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format=('%d/%m/%Y',)), input_formats=DATE_INPUT_FORMATS)
    comment = forms.CharField(required=False)

    class Meta:
        model = Reservation
        fields = [
            'room',
            'date',
            'comment',
        ]

    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= datetime.now().date():
            raise forms.ValidationError('Can not add reservation with date from the past')
        return date
