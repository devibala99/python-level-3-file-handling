from storage import create_user, authenticate_user


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    success, message = create_user(username, password)
    print(message)


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    success, result = authenticate_user(username, password)

    if not success:
        print(result)
        return

    print(f"\nWelcome {username}")
    user_vault(result)


def user_vault(user_data):
    while True:
        print("\n1. View Vault")
        print("2. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("Your Vault Data:", user_data["vault"])
        elif choice == "2":
            break
        else:
            print("Invalid choice")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
