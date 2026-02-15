# Django Backend Integration Guide

## Overview
RapidRescue now includes a Django backend with REST API endpoints for emergency requests and hospital management.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the Application

#### Option 1: Using the Enhanced Run Script (Recommended)
```bash
python run_django.py
```
This will:
- Install dependencies if needed
- Run database migrations
- Start Django backend on port 8001
- Start frontend on port 8000
- Open browser automatically

#### Option 2: Manual Setup
Start Django backend:
```bash
python manage.py runserver 8001
```

Start frontend (in separate terminal):
```bash
python run_app.py
```

## API Endpoints

### Emergency Services
- `GET /api/emergency/emergency-requests/` - List all emergency requests
- `POST /api/emergency/emergency-requests/` - Create new emergency request
- `POST /api/emergency/emergency-requests/{id}/accept/` - Accept emergency request
- `POST /api/emergency/emergency-requests/{id}/resolve/` - Resolve emergency request
- `GET /api/emergency/emergency-requests/nearby/?lat=X&lng=Y&radius=Z` - Get nearby emergencies

### Hospital Services
- `GET /api/hospitals/hospitals/` - List all hospitals
- `GET /api/hospitals/hospitals/nearby/?lat=X&lng=Y&radius=Z` - Get nearby hospitals
- `GET /api/hospitals/hospitals/{id}/` - Get hospital details
- `GET /api/hospitals/hospitals/{id}/departments/` - Get hospital departments
- `POST /api/hospitals/hospitals/{id}/add_review/` - Add hospital review
- `GET /api/hospitals/hospitals/{id}/reviews/` - Get hospital reviews

## Frontend Integration

The frontend now includes:
- `api.js` - API service classes for backend communication
- Updated `script.js` with async functions for API calls
- Location services integration
- Real-time emergency activation

## Features

### Emergency Management
- Create emergency requests with location data
- Track emergency status (pending, accepted, in_progress, resolved)
- Real-time emergency response tracking

### Hospital Management
- Find nearby hospitals based on location
- View hospital details and departments
- Read and write hospital reviews
- Filter hospitals by services and availability

### Location Services
- Automatic geolocation detection
- Address resolution from coordinates
- Distance-based searches

## Development

### Admin Panel
Access Django admin at `http://localhost:8001/admin/`
- Default superuser: Create with `python manage.py createsuperuser`

### Database Models
- `EmergencyRequest` - Emergency incidents
- `EmergencyResponse` - Response tracking
- `Hospital` - Medical facilities
- `HospitalDepartment` - Hospital departments
- `HospitalReview` - User reviews

## Configuration

### CORS Settings
Backend configured to accept requests from `localhost:8000` and `127.0.0.1:8000`

### API Base URL
Frontend configured to connect to `http://localhost:8001/api`

## Troubleshooting

1. **Port conflicts**: Change ports in `run_django.py` if needed
2. **CORS errors**: Ensure frontend URL is in `CORS_ALLOWED_ORIGINS`
3. **Database errors**: Run migrations again with `python manage.py migrate`
4. **Dependencies**: Install with `pip install -r requirements.txt`
