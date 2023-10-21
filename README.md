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

![Screenshot_20230513-144330-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/a580f8a1-10c6-46fe-ad3c-6533179df474)
![Screenshot_20230513-131735-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/9ffe7b96-45c4-4800-832a-291f02f6739a)
![Screenshot_20230513-135553-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/70bd1208-c3d7-4878-9747-d9290b2181e2)
![Screenshot_20230513-140710-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/28225b5c-37aa-4726-a374-924d3fc2d8ea)
![Screenshot_20230513-140743-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/3ece968e-b435-4a6e-94ae-b54a16f64cab)
![Screenshot_20230513-135458-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/e5c6d872-eda8-4c29-bb75-a1f993c2bbbc)
![Screenshot_20230513-150759-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/63259489-8366-42fc-a7b7-adc1f9bf0c45)
![Screenshot_20230513-134222-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/9e1ba38b-74d7-4a28-9dbf-4abc74b24202)
![Screenshot_20230513-143315-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/7f227f25-e575-4e6e-8e45-6f9b3e161bd8)
![Screenshot_20230513-143357-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/998562df-f1dd-4ce6-8db9-5529af37a79b)
![Screenshot_20230513-143739-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/ad510dc1-d7f4-4640-a41c-2b76bb765a66)
![Screenshot_20230513-143857-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/e4d2d137-4ea9-4cc5-a2d1-9be2d1316d22)
![Screenshot_20230513-140928-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/ec466f0b-d30e-4630-b566-7d1c0c89244c)
![Screenshot_20230513-141511-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/d7c5ed96-f2c9-4b02-b765-458646d1f58c)
![Screenshot_20230513-142758-portrait](https://github.com/SuhailMuhammed1/Hospital-App-Using-Flutter-With-Django-Mysql-REST-API/assets/104970300/1e003b2a-fbda-48b8-ba81-8c2e21f683b4)
