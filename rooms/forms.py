from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'check_in', 'check_out', 'guests', 'notes']
