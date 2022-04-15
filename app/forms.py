
from django import forms
from django.forms import ModelForm
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['full_name','source','destination','booking_date','quantity']
        # widgets = {
        #     'full_name': forms.TextInput(attrs ={'class':'form-control','placeholder':'Full name'}),
        #     'quantity': forms.TextInput(attrs ={'class':'form-control','placeholder':'Amount of tickets '}),
        #     'source': forms.TextInput(attrs ={'class':'form-check-input','placeholder':'Source'}),
        #     'destination': forms.TextInput(attrs ={'class':'form-control','placeholder':'Destination'}),
        #     'booking_date': forms.DateInput(attrs={'class':'form-control','placeholder':'Date of tickets'})
        # }
        # labels = {
        #     'full_name': '',
        #     'quantity': '',
        #     'source': '',
        #     'destination': '',
        #     'booking_date': ''
        # }