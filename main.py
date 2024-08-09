import os
import django
import random
from decimal import Decimal
from booking.models import Room, Booking
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_booking.settings")
django.setup()

User = get_user_model()


def create_users(num_users):
    users = []
    for i in range(num_users):
        username = f"user_{i}"
        email = f"user_{i}@example.com"
        user = User.objects.create_user(
            username=username, email=email, password="password"
        )
        users.append(user)
    return users


def create_user(username, email, password):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password)
    print(f"Created user: {username}, Email: {email}")
    return user


def create_rooms(num_rooms):
    room_names = [
        "Cozy Cottage",
        "Luxury Villa",
        "Modern Apartment",
        "Downtown Studio",
        "Suburban House",
        "Beachfront Bungalow",
        "Mountain Cabin",
        "Country House",
        "Urban Loft",
        "Penthouse Suite",
        "Garden Flat",
        "Lake House",
        "Historic Manor",
        "Ski Chalet",
        "Desert Oasis",
        "City Condo",
        "Rural Retreat",
        "Forest Lodge",
        "Seaside Cottage",
        "Countryside B&B",
        "Island Villa",
        "Eco-friendly Home",
        "High-rise Apartment",
        "Vintage Caravan",
        "Castle",
        "Riverside Cabin",
        "Luxury Tent",
        "Houseboat",
        "Studio Apartment",
        "Bamboo Hut",
        "Geodesic Dome",
        "Cave House",
        "Treehouse",
        "Victorian Home",
        "Retro Camper",
        "Modern Loft",
        "Barn Conversion",
        "Chateau",
        "Tiny House",
        "Hunting Lodge",
        "Country Estate",
        "Urban Penthouse",
        "Hillside Villa",
        "Fishing Cabin",
        "Rustic Barn",
        "Safari Tent",
        "Artistic Studio",
        "Clifftop House",
        "Subterranean Home",
        "City Flat",
    ]

    for i in range(num_rooms):
        name = f"{random.choice(room_names)} {i+1}"
        price_per_night = Decimal(
            random.uniform(
                50, 500)).quantize(
            Decimal("0.01"))
        capacity = random.randint(1, 10)

        Room.objects.create(
            name=name, price_per_night=price_per_night, capacity=capacity
        )
        print(
            f"Created room: {name}, Price: ${price_per_night}, Capacity: {capacity}")


def create_room(name="Cozy Cottage", price_per_night=100, capacity=5):
    room = Room.objects.create(
        name=name, price_per_night=price_per_night, capacity=capacity
    )
    print(
        f"Created room: {name}, Price: ${price_per_night}, Capacity: {capacity}")
    return room


def delete_room(room_id):
    try:
        room = Room.objects.get(id=room_id)
        room.delete()
        print(f"Deleted room with ID: {room_id}")
    except Room.DoesNotExist:
        print(f"Room with ID: {room_id} does not exist")


def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        print(f"Deleted user with ID: {user_id}")
    except User.DoesNotExist:
        print(f"User with ID: {user_id} does not exist")


def delete_all_users():
    User.objects.all().delete()
    print("Deleted all users")


def delete_booking(booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.delete()
        print(f"Deleted booking with ID: {booking_id}")
    except Booking.DoesNotExist:
        print(f"Booking with ID: {booking_id} does not exist")


def delete_all_rooms():
    Room.objects.all().delete()
    print("Deleted all rooms")


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Create rooms")
        print("2. Create users")
        print("3. Create a room")
        print("4. Create a user")
        print("5. Delete a room")
        print("6. Delete a user")
        print("7. Delete all rooms")
        print("8. Delete all users")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_rooms = int(input("Enter number of rooms to create: "))
            create_rooms(num_rooms)
        elif choice == "2":
            num_users = int(input("Enter number of users to create: "))
            create_users(num_users)
        elif choice == "3":
            name = input("Enter room name: ")
            price_per_night = Decimal(input("Enter price per night: "))
            capacity = int(input("Enter capacity: "))
            create_room(name, price_per_night, capacity)
        elif choice == "4":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            create_user(username, email, password)
        elif choice == "5":
            room_id = int(input("Enter room ID to delete: "))
            delete_room(room_id)
        elif choice == "6":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == "7":
            delete_all_rooms()
        elif choice == "8":
            delete_all_users()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")
