seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seat numbers with current status
for index, status in enumerate(seats, start=1):
    print(f"Seat {index}: {status}")

# Ask user to enter a seat number
seat_number = int(input("\nEnter seat number to book: "))

# Validate and process booking (converting 1-based seat number to 0-based index)
if 1 <= seat_number <= len(seats):
    if seats[seat_number - 1] == "Available":
        seats[seat_number - 1] = "Booked"
        print("Seat booked successfully.")
    else:
        print("Seat is already booked.")
else:
    print("Invalid seat number.")

# Calculate summary counts
total_seats = len(seats)
booked_seats = seats.count("Booked")
available_seats = seats.count("Available")

# Display final summary
print(f"\nTotal Seats: {total_seats}")
print(f"Booked Seats: {booked_seats}")
print(f"Available Seats: {available_seats}")
