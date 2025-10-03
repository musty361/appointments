from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Appointment
from .forms import AppointmentForm

def create_appointment(request):
    """View for creating a new appointment."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(
                request,
                f'Appointment booked successfully! Your appointment ID is {appointment.id}'
            )
            return redirect('appointments:checkout', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'title': 'Book an Appointment'
    }
    return render(request, 'appointments/appointment_form.html', context)

def checkout(request, appointment_id):
    """View for displaying payment form."""
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Mock service pricing
    service_prices = {
        'consultation': 50.00,
        'cleaning': 150.00,
        'repair': 300.00,
        'maintenance': 75.00,
    }

    amount = service_prices.get(appointment.service_type.lower(), 100.00)

    context = {
        'appointment': appointment,
        'title': 'Payment',
        'amount': amount,
        'appointmentId': appointment_id
    }
    return render(request, 'appointments/payment.html', context)

def process_payment(request, appointment_id):
    """View for processing mock payment."""
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)

        # Mock payment processing - always successful
        # In a real app, this would integrate with Stripe API
        appointment.status = 'confirmed'
        appointment.save()

        return redirect('payment_success', appointment_id=appointment.id)

    return redirect('checkout', appointment_id=appointment_id)

def payment_success(request, appointment_id):
    """View for displaying payment success confirmation."""
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Mock payment details
    payment_id = f"pi_{appointment.id}_mock_payment_{appointment.id}"

    context = {
        'appointment': appointment,
        'title': 'Payment Successful',
        'payment_id': payment_id
    }
    return render(request, 'appointments/payment_success.html', context)

def appointment_list(request):
    """View for displaying all appointments (optional admin view)."""
    appointments = Appointment.objects.all()

    context = {
        'appointments': appointments,
        'title': 'All Appointments'
    }
    return render(request, 'appointments/appointment_list.html', context)
