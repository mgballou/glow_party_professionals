from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Create your models here.

CITIES = (
    ('*', ''),
    ('N', 'New York'),
    ('M', 'Miami'),
    ('L', 'Los Angeles'),
    ('W', 'Washington, D.C.'),
    ('V', 'Las Vegas')
)

class Subscription(models.Model):
    email = models.CharField(max_length=100, null=False, unique=True)
    city = models.CharField(max_length=1, 
                            choices=CITIES,
                            default=CITIES[0][0])

    def __str__(self):
        return self.email
    
class Booking(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = PhoneNumberField()
    email = models.EmailField(null=False, max_length=254)
    date = models.DateField(null=False)
    event_description = models.TextField(max_length=500)
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('confirm', kwargs={'booking_id': self.id})


