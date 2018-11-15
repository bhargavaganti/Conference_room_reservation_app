from django import forms
from datetime import datetime
from .models import Room, Reservation

DATE_FORMATS = (
    '%d/%m/%Y',
    '%d-%m-%Y',
    '%d.%m.%Y',
    '%d %m %Y',
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


class ReservationCreateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format=('%d/%m/%Y',)), input_formats=DATE_FORMATS)
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
            raise forms.ValidationError('Can not add reservation with past date')
        return date
