
from django.contrib import admin
from .models import Department, PatientProfile, DoctorProfile, Appointment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'gender')
    search_fields = ('user__username', 'phone')


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'department',
        'specialization',
        'experience_years',
        'consultation_fee',
        'is_available'
    )
    list_filter = ('department', 'is_available')
    search_fields = ('user__username', 'specialization')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status'
    )
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__user__username', 'doctor__user__username')

