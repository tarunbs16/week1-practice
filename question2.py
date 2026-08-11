customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
num_tickets = int(input("Enter number of tickets: "))

# Ticket price rules based on age
if age < 12:
    ticket_price = 120
elif age <= 59:
    ticket_price = 200
else:
    ticket_price = 150

# Calculate total before discount
total_before_discount = ticket_price * num_tickets

# Apply 10% discount if 5 or more tickets are purchased
if num_tickets >= 5:
    discount = 0.10 * total_before_discount
else:
    discount = 0

final_amount = total_before_discount - discount

# Display details
print("\n--- Ticket Bill Summary ---")
print("Customer Name:", customer_name)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", num_tickets)
print("Total Before Discount:", total_before_discount)
print("Discount:", discount)
print("Final Amount:", final_amount)
