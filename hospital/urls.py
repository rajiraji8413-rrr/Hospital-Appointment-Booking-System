
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Home page
    path('', views.home, name='home'),

    # Doctor listing
    path('doctors/', views.doctor_list, name='doctor_list'),

    # Book appointment
    path(
        'doctors/<int:doctor_id>/book/',
        views.book_appointment,
        name='book_appointment'
    ),

    # Patient appointments
    path(
        'my-appointments/',
        views.my_appointments,
        name='my_appointments'
    ),

    # Doctor dashboard
    path(
        'doctor-dashboard/',
        views.doctor_dashboard,
        name='doctor_dashboard'
    ),

    # Update appointment status
    path(
        'appointments/<int:appointment_id>/status/',
        views.update_appointment_status,
        name='update_appointment_status'
    ),

    # Patient registration
    path(
        'register/',
        views.patient_register,
        name='patient_register'
    ),

    # Patient profile
    path(
        'patient-profile/',
        views.patient_profile,
        name='patient_profile'
    ),

    # Admin dashboard
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='hospital/login.html'
        ),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

]
