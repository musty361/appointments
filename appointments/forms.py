from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    """Form for creating and editing appointments."""

    class Meta:
        model = Appointment
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'appointment_date',
            'appointment_time',
            'service_type',
            'notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('consultation', 'Consultation'),
                ('follow_up', 'Follow-up Visit'),
                ('vaccination', 'Vaccination'),
                ('check_up', 'General Check-up'),
                ('dental_cleaning', 'Dental Cleaning'),
                ('other', 'Other')
            ]),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any additional notes or special requirements'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields required except notes
        for field_name in self.fields:
            if field_name != 'notes':
                self.fields[field_name].required = True

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')

        # Add any custom validation here if needed
        if appointment_date and appointment_time:
            # You could add logic here to check for appointment conflicts
            pass

        return cleaned_data
