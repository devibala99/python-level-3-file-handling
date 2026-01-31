from ticket_service import create_ticket, update_ticket_state

def main():
    print("1. Create Ticket")
    print("2. Update Ticket State")

    choice = input("Choose option: ")

    if choice == "1":
        ticket_id = input("Ticket ID: ")
        desc = input("Description: ")
        success, msg = create_ticket(ticket_id, desc)
        print(msg)

    elif choice == "2":
        ticket_id = input("Ticket ID: ")
        new_state = input("New State (IN_PROGRESS / RESOLVED): ")
        success, msg = update_ticket_state(ticket_id, new_state)
        print(msg)

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
