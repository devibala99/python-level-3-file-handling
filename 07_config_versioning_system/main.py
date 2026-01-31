from config_manager import (
    create_new_config,
    set_active_version,
    list_versions,
    read_active_config
)

def main():
    while True:
        print("\n1. Create New Config")
        print("2. Switch Active Version")
        print("3. View Active Config")
        print("4. List Versions")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            key = input("Config key: ")
            value = input("Config value: ")
            version = create_new_config({key: value})
            print(f"Config saved as version v{version}")

        elif choice == "2":
            v = int(input("Enter version number: "))
            success, msg = set_active_version(v)
            print(msg)

        elif choice == "3":
            config = read_active_config()
            print(config if config else "No active config")

        elif choice == "4":
            print("Available versions:", list_versions())

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
