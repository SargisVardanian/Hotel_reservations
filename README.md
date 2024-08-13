# Hotel Reservations

This is a Django-based project for managing hotel room bookings. The project provides APIs for creating, updating, and querying room bookings and availability.

## Features

- User authentication and registration
- Room management (create, update, delete, and view rooms)
- Booking management (create, update, delete, and view bookings)
- API for querying available rooms within a specified date range
- Filtering rooms by capacity, price per night, and availability
- Admin interface for managing rooms and bookings

## Setup

### Prerequisites

- Python 3.10
- Django 5.0.7
- Django REST framework
- Django Filters

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SargisVardanian/Hotel_reservations.git
    cd Hotel_reservations
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/admin` to access the admin interface and start managing your hotel bookings.

## API Endpoints

### Rooms

- `GET /api/rooms/` - List all rooms.
- `POST /api/rooms/` - Create a new room.
- `GET /api/rooms/{id}/` - Retrieve a room by ID.
- `PUT /api/rooms/{id}/` - Update a room by ID.
- `DELETE /api/rooms/{id}/` - Delete a room by ID.
- `GET /api/rooms/available/` - List all available rooms within a specified date range.

### Bookings

- `GET /api/bookings/` - List all bookings.
- `POST /api/bookings/` - Create a new booking.
- `GET /api/bookings/{id}/` - Retrieve a booking by ID.
- `PUT /api/bookings/{id}/` - Update a booking by ID.
- `DELETE /api/bookings/{id}/` - Delete a booking by ID.

## Filters

You can filter the available rooms using the following query parameters:

- `capacity`: Exact capacity of the room.
- `min_price`: Minimum price per night.
- `max_price`: Maximum price per night.
- `check_in`: Check-in date (YYYY-MM-DD).
- `check_out`: Check-out date (YYYY-MM-DD).

Example:

```http
GET /api/rooms/available/?capacity=2&min_price=100&max_price=200&check_in=2024-07-18&check_out=2024-07-20
