from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Booking, Subscription
from .forms import BookingForm, SubscriptionForm

# Create your views here.
def home(request):
    subscription_form = SubscriptionForm()
    return render(request, 'home.html', {'subscription_form': subscription_form})

def about(request):
    return render(request, 'about.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def booking(request):
    return render(request, 'booking.html')

class BookingCreate(CreateView):
    model = Booking
    form_class = BookingForm
  
    def form_valid(self, form):
        return super().form_valid(form)