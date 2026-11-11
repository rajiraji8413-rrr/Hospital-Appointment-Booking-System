
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Appointment, PatientProfile


# =====================================
# 1. APPOINTMENT FORM
# =====================================

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'appointment_date',
            'appointment_time',
            'reason',
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

            'reason': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter reason for consultation',
                    'rows': 4
                }
            ),
        }


# =====================================
# 2. PATIENT REGISTRATION FORM
# =====================================

class PatientRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )

    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })
    )

    gender = forms.ChoiceField(
        choices=[
            ('', 'Select Gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your address',
            'rows': 3
        })
    )

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'address',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
        }

# =====================================
# 3. PATIENT PROFILE FORM
# =====================================

class PatientProfileForm(forms.ModelForm):

    class Meta:
        model = PatientProfile

        fields = [
            'phone',
            'date_of_birth',
            'gender',
            'address',
        ]

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),

            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 3
            }),
        }

