from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id) # can also use pk for primary key instead of id
    return render(request, "flights/flight.html", {
        "flight": flight, "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        non_passengers = Passenger.objects.exclude(flights=flight).all()
        return render(request, "flights/flight.html", {
            "flight": flight, "passengers": flight.passengers.all(),
            "non_passengers": non_passengers
        })
    
def remove(request, flight_id):
    print("In the remove")
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.remove(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))