from django import forms
from .models import Booking, Subscription

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        # fields = ('first_name', 'last_name', 'phone','email', 'preferred_date', 'alternate_date1', 'alternate_date2', 'event_description','number_of_guests')
        
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'email'}),
            'date': forms.DateInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'date'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'event description'}),
            'number_of_guests': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'number of guests'})
            

        }

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription

        fields = '__all__'

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'email'}),
            'city': forms.Select(attrs={'class': 'form-control border border-dark border-2 rounded-3', 'placeholder': 'city'}),



        }