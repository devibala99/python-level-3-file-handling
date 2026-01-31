from event_logger import log_event
from event_reader import read_all_events, read_events_by_user


def main():
    while True:
        print("\n1. Add Event")
        print("2. View All Events")
        print("3. View Events by User")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            user = input("User: ")
            action = input("Action (MESSAGE / LOGIN / LOGOUT): ")
            data = input("Data: ")
            log_event(user, action, data)
            print("Event logged")

        elif choice == "2":
            events = read_all_events()
            for e in events:
                print(e)

        elif choice == "3":
            user = input("Username: ")
            events = read_events_by_user(user)
            for e in events:
                print(e)

        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
