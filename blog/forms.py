from django import forms
from .models import Review, Appointment
from django.forms.widgets import DateInput
from datetime import date

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "phone", "content", "grade", "master"]

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        label='Выберите дату',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    appointment_time = forms.ChoiceField(
        label='Выберите время',
        choices=[(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(9, 22) for minute in range(0, 60, 30)],
    )

    class Meta:
        model = Appointment
        fields = ['service', 'master','appointment_date', 'appointment_time']
        widgets = {
            'appointment_date': DateInput(attrs={'type': 'date', 'min': date.today()}),
        }