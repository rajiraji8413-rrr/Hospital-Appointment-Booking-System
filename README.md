# Hospital Appointment Booking System

A web-based Hospital Appointment Booking System developed using Django and MySQL. This application helps patients find doctors, register, manage their profiles, and book appointments online.

## Features

- **Doctor Management:** Create doctor accounts and manage qualifications, specializations, experience, departments, and consultation fees.
- **Patient Registration and Login:** Patients can register and securely log in.
- **Doctor Listing:** View available doctors and filter by department.
- **Appointment Booking:** Patients can select doctors and book appointments.
- **Appointment Management:** Doctors can confirm, cancel, or complete appointments.
- **Patient Profile Management:** Patients can view and update their profile details.
- **Admin Dashboard:** View doctors, patients, departments, appointments, and pending appointments.
- **Doctor Dashboard:** Doctors can view and manage their appointments.

## Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- Bootstrap
- JavaScript

## Project Structure

```text
Hospital-Appointment-Booking-System/
│
├── hospital/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── hospital_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/rajiraji8413-rrr/Hospital-Appointment-Booking-System.git
```

2. Open the project folder:

```bash
cd Hospital-Appointment-Booking-System
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Create a MySQL database named `hospital_db`.

7. Configure your database credentials and Django secret key using your local environment settings. Do not upload private credentials to GitHub.

8. Run database migrations:

```bash
python manage.py migrate
```

9. Create an administrator account:

```bash
python manage.py createsuperuser
```

10. Start the development server:

```bash
python manage.py runserver
```

11. Open the application:

http://127.0.0.1:8000/

## Future Improvements

- Email notifications for appointment updates.
- Doctor availability and appointment scheduling improvements.
- Enhanced reporting and analytics.

## Author

GitHub: https://github.com/rajiraji8413-rrr

## License

This project is created for learning and portfolio purposes.
