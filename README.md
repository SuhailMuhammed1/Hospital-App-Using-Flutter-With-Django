# Hospital App using Flutter with Django and MySQL REST API

## Introduction

This repository contains the source code for a hospital management application developed using the Flutter framework for the front-end, Django for the back-end, and MySQL as the database. The app is designed to streamline hospital management processes, allowing staff to manage patient information, appointments, and more efficiently.

## Features

* Patient Management: Easily add, edit, and view patient details.
* Appointment Scheduling: Schedule and manage appointments for patients.
* Doctor and Staff Management: Maintain records of hospital staff and doctors.
* Lab Records: Securely store and access patient lab records.
* User Authentication: Secure user accounts and role-based access control.
  
## Technologies Used

* Front-end: Flutter
* Back-end: Django
* Database: MySQL
* REST API: Django REST framework

## Step 1: Installation

1. Setup the Django Back-end:

* Navigate to the backend directory.
* Create a virtual environment: python -m venv venv
* Activate the virtual environment: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows).
* Start the Django development server: python manage.py runserver

2. Setup the MySQL Database:

* Navigate to the Dump20230515 file on directory.
* Install Xampp and open it.
* Create a Database.
* DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your database name',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': ''
    }
} 
* Configure your MySQL database settings in backend/hospital/settings.py.
* Run migrations: python manage.py migrate

3. Setting Up the Flutter Front-end:

* Open the Flutter Project:
  * Open the frontend directory of your project in your Flutter development environment, such as Android Studio, Visual Studio Code, or the command line.

* Install Flutter Dependencies:
  * Run the following command to fetch the Flutter project dependencies:
    * flutter pub get

* Run the Flutter App:
  * Launch the Flutter app by running the following command within the frontend directory:
    * flutter run

## Step 2: Usage

* Open the Flutter app and sign in with your credentials.
* Explore the app's features and functionalities.
* Create doctors, patients, schedule appointments, manage profile, and more.

## Screenshots


