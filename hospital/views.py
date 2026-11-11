
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import (
    DoctorProfile,
    Department,
    PatientProfile,
    Appointment
)

from .forms import (
    AppointmentForm,
    PatientRegistrationForm,
    PatientProfileForm
)


# ----------------------------------
# 1. HOME PAGE
# ----------------------------------

def home(request):

    context = {
        'is_admin': request.user.is_superuser,
        'is_doctor': hasattr(request.user, 'doctor_profile'),
        'is_patient': hasattr(request.user, 'patient_profile'),
    }

    return render(request, 'hospital/home.html', context)


# ----------------------------------
# 2. DOCTOR LIST
# ----------------------------------

def doctor_list(request):

    doctors = DoctorProfile.objects.select_related(
        'user',
        'department'
    ).filter(is_available=True)

    departments = Department.objects.all()

    search = request.GET.get('search', '')
    department_id = request.GET.get('department', '')

    if search:
        doctors = doctors.filter(
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(specialization__icontains=search)
        )

    if department_id:
        doctors = doctors.filter(department_id=department_id)

    context = {
        'doctors': doctors,
        'departments': departments,
        'search': search,
        'selected_department': department_id,
    }

    return render(request, 'hospital/doctor_list.html', context)


# ----------------------------------
# 3. BOOK APPOINTMENT
# ----------------------------------

@login_required(login_url='login')
def book_appointment(request, doctor_id):

    doctor = get_object_or_404(
        DoctorProfile,
        id=doctor_id,
        is_available=True
    )

    patient = get_object_or_404(
        PatientProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.doctor = doctor

            try:
                appointment.save()
                messages.success(
                    request,
                    'Your appointment has been booked successfully!'
                )
                return redirect('my_appointments')

            except Exception:
                messages.error(
                    request,
                    'This doctor already has an appointment at that date and time. Please choose another slot.'
                )

    else:
        form = AppointmentForm()

    context = {
        'doctor': doctor,
        'form': form,
    }

    return render(
        request,
        'hospital/book_appointment.html',
        context
    )


# ----------------------------------
# 4. MY APPOINTMENTS
# ----------------------------------

@login_required(login_url='login')
def my_appointments(request):

    patient = get_object_or_404(
        PatientProfile,
        user=request.user
    )

    appointments = Appointment.objects.select_related(
        'doctor__user',
        'doctor__department'
    ).filter(patient=patient)

    context = {
        'appointments': appointments,
    }

    return render(
        request,
        'hospital/my_appointments.html',
        context
    )


# ----------------------------------
# 5. DOCTOR DASHBOARD
# ----------------------------------

@login_required(login_url='login')
def doctor_dashboard(request):

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    appointments = Appointment.objects.select_related(
        'patient__user'
    ).filter(doctor=doctor)

    context = {
        'doctor': doctor,
        'appointments': appointments,
    }

    return render(
        request,
        'hospital/doctor_dashboard.html',
        context
    )


# ----------------------------------
# 6. UPDATE APPOINTMENT STATUS
# ----------------------------------

@login_required(login_url='login')
@require_POST
def update_appointment_status(request, appointment_id):

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )

    new_status = request.POST.get('status')

    allowed_statuses = [
        'Confirmed',
        'Cancelled',
        'Completed'
    ]

    if appointment.status in ['Completed', 'Cancelled']:
        messages.error(
            request,
            'This appointment has already been closed.'
        )

    elif new_status not in allowed_statuses:
        messages.error(
            request,
            'Invalid appointment status.'
        )

    else:
        appointment.status = new_status
        appointment.save()

        messages.success(
            request,
            f'Appointment status updated to {new_status}.'
        )

    return redirect('doctor_dashboard')


# ----------------------------------
# 7. PATIENT REGISTRATION
# ----------------------------------

def patient_register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = PatientRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']

            user.save()

            PatientProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                gender=form.cleaned_data['gender'],
                address=form.cleaned_data['address']
            )

            messages.success(
                request,
                'Your patient account has been created successfully! Please log in.'
            )

            return redirect('login')

    else:
        form = PatientRegistrationForm()

    return render(
        request,
        'hospital/register.html',
        {'form': form}
    )


# ----------------------------------
# 8. PATIENT PROFILE
# ----------------------------------

@login_required(login_url='login')
def patient_profile(request):

    patient = get_object_or_404(
        PatientProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = PatientProfileForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your profile has been updated successfully!'
            )

            return redirect('patient_profile')

    else:
        form = PatientProfileForm(instance=patient)

    context = {
        'form': form,
        'patient': patient,
    }

    return render(
        request,
        'hospital/patient_profile.html',
        context
    )


# ----------------------------------
# 9. ADMIN DASHBOARD
# ----------------------------------

@login_required(login_url='login')
def admin_dashboard(request):

    # Only superusers can access this dashboard
    if not request.user.is_superuser:

        messages.error(
            request,
            'You are not authorized to access this page.'
        )

        return redirect('home')

    # Total doctors
    total_doctors = DoctorProfile.objects.count()

    # Total patients
    total_patients = PatientProfile.objects.count()

    # Total departments
    total_departments = Department.objects.count()

    # Total appointments
    total_appointments = Appointment.objects.count()

    # Pending appointments
    pending_appointments = Appointment.objects.filter(
        status='Pending'
    ).count()

    # Latest five appointments
    recent_appointments = Appointment.objects.select_related(
        'patient__user',
        'doctor__user',
        'doctor__department'
    ).order_by('-created_at')[:5]

    context = {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_departments': total_departments,
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'recent_appointments': recent_appointments,
    }

    return render(
        request,
        'hospital/admin_dashboard.html',
        context
    )
