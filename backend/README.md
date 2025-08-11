# Appointment Booking System

A simple FastAPI-based web app for booking appointments with JWT authentication and role-based access control.

## Prerequisites
* Python 3.13
* pip package manager

## Setup & Run
```
pip install --upgrade pip
pip install -r requirements.txt
```

## Start the app
`uvicorn app.main:app --reload`

The server will run at: http://127.0.0.1:8000
Usage
API Docs

    Swagger UI → http://127.0.0.1:8000/docs

    ReDoc → http://127.0.0.1:8000/redoc

**Default Accounts: <br>**

| Username | Password  | Role  |
|----------|-----------|-------|
| admin    | admin123  | Admin |
| alice    | alice123  | User  |