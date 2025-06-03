# Car Rental Web Application

## Overview
This is a Django-based web application designed to manage the operations of a small car rental company. The application supports user registration and authentication with roles, car management, booking management, payment simulation, search and filtering, and features a responsive and modern user interface.

---

## Features

- **User Authentication and Roles**
  - User registration, login, and logout for both customers and admins.
  - Admin dashboard to manage cars, customers, and bookings.
  - Customer dashboard to view bookings and profile information.

- **Car Management**
  - Admin can add, update, and delete car records.
  - Each car has details like make, model, year, registration number, price per day, availability, and optional images.
  - Customers can browse available cars with filter options and view details.

- **Booking Management**
  - Customers can book cars for specific rental periods.
  - Bookings track start/end dates, customer, and car details.
  - Admin can view, confirm, cancel, or modify bookings.
  - Customers can view booking history and status.

- **Payment Integration**
  - Simulated payment process for bookings including booking confirmation, invoice, and receipt generation.

- **Search and Filter**
  - Customers can search cars by make, model, price range, and availability.
  - Admin can filter bookings by customer name, status, or date range.

- **Responsive Design**
  - Clean, intuitive, and responsive UI for desktop and mobile devices.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (recommended)
  
### Steps to Run the Project

1. **Clone the repository (i dont have for now):**
   ```bash
   git clone <repository-url>
   cd webpro/car_rental

2.Create and activate a virtual environment:

bash
Run
Copy code
python3 -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
3.Install dependencies:

bash
Run
Copy code
pip install -r requirements.txt

4.Apply migrations:

bash
Run
Copy code
python manage.py migrate

5. Create a superuser to access the admin panel:

bash
Run
Copy code
python manage.py createsuperuser
6. Run the development server:

bash
Run
Copy code
python manage.py runserver
7.Access the app:

Open your browser and navigate to: http://127.0.0.1:8000/
Admin interface: http://127.0.0.1:8000/admin

User Manuals
Admin Manual
Login with your admin credentials at http://127.0.0.1:8000/admin.
Manage cars: add, edit, or delete car records including images and availability status.
View and manage all bookings — confirm, cancel or modify booking statuses.
Manage users if needed.

Customer Manual
Register and log in through the front end.
Browse available cars, filter by make, model, price, and availability.
Book cars for selected periods.
View your booking history and statuses in the customer dashboard.
Simulated payment during booking confirms and generates an invoice.

Thank you for using the Car Rental Web Application!