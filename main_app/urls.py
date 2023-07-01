from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('booking/', views.booking, name='booking')
]