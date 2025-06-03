from django.shortcuts import render
from django.urls import path
from django.shortcuts import render, redirect
from models import Car
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from .models import Booking, Car, Feedback, Payment
from .forms import BookingForm, FeedbackForm

def register(request):
    return render(request, 'My_Car_rental/register.html')

def login_view(request):
    return render(request, 'My_Car_rental/login.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'My_Car_rental/car_list.html', {'cars': cars})

def index(request):
    return render(request, 'index.html')

    query = request.GET.get('q', '').strip()
    make = request.GET.get('make', '')
    model = request.GET.get('model', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')
    qs = Car.objects.all()
    if query:
        qs = qs.filter(Q(make__icontains=query) | Q(model__icontains=query))
    if make:
        qs = qs.filter(make__iexact=make)
    if model:
        qs = qs.filter(model__iexact=model)
    if min_price:
        qs = qs.filter(price_per_day__gte=min_price)
    if max_price:
        qs = qs.filter(price_per_day__lte=max_price)
    if available == 'true':
        qs = qs.filter(availability=True)
    cars_list = list(qs.values('id', 'make', 'model', 'year', 'registration_number', 'price_per_day', 'availability'))
    return JsonResponse({'cars': cars_list})

