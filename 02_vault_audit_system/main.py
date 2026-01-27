from storage import (
    create_user,
    authenticate_user,
    add_vault_item
)

def user_vault(username, user_data):
    while True:
        print("\n1. View Vault")
        print("2. Add Vault Item")
        print("3. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("Your Vault:", user_data["vault"])

        elif choice == "2":
            item = input("Enter vault item: ")
            success, message = add_vault_item(username, item)
            print(message)

            # Reload fresh state after write
            password = input("Re-enter password: ")
            success, user_data = authenticate_user(username, password)
            if not success:
                print("Session expired")
                break

        elif choice == "3":
            break

        else:
            print("Invalid option")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            success, message = create_user(username, password)
            print(message)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            success, result = authenticate_user(username, password)

            if success:
                print("Login successful")
                user_vault(username, result)
            else:
                print(result)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
