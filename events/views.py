from django.shortcuts import render, get_object_or_404
from .models import Event, Registration


def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {
        'events': events
    })


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {
        'event': event
    })


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']

        Registration.objects.create(
            event=event,
            name=name,
            email=email
        )

        return render(request, 'events/register_success.html')

    return render(request, 'events/register.html', {
        'event': event
    })


def registrations(request):
    registrations = Registration.objects.all()
    return render(request, 'events/registrations.html', {
        'registrations': registrations
    })


def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    registration.delete()
    return render(request, 'events/cancel_success.html')