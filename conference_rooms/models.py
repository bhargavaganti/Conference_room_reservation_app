from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(validators=[MinValueValidator(10), ])
    projector_is_available = models.BooleanField(default=True, verbose_name='projector')
    is_active = models.BooleanField(default=True, verbose_name='active')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('room-detail-view', kwargs={'id': self.id})


class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('date', 'room')

    def __str__(self):
        return f'{self.room} on {self.date}'

    def get_absolute_url(self):
        return reverse('reservation-detail-view', kwargs={'id':self.id})