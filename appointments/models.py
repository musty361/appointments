from django.db import models

class Appointment(models.Model):
    """Model representing an appointment booking."""

    # Customer Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Appointment Details
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service_type = models.CharField(max_length=100)

    # Additional Information
    notes = models.TextField(blank=True, null=True)

    # Status and timestamps
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date} {self.appointment_time}"

    def get_full_name(self):
        """Return the full name of the customer."""
        return f"{self.first_name} {self.last_name}"
