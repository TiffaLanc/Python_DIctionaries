# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
 }

def new_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

def update_ticket(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status

def display_ticket(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f'{ticket_id}: {details["Customer"]}', {details["Issue"]} , {details["Status"]})


new_ticket("Ticket003", "Ben", "Connectivity intermittent")

update_ticket("Ticket001", "closed")

print("All Tickets:")
display_ticket()

print("\nOpen tickets:")
display_ticket("open")

print("\nClosed tickets:")
display_ticket("closed")

