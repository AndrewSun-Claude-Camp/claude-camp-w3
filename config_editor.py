# Json Configuration Editor
import json
import sys

Config_File = "config.json"

def read_config():
    try:
        with open(Config_File, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{Config_File} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def save_config(config):
    with open(Config_File, "w") as file:
        json.dump(config, file, indent=4)
    print(f"\nPreferences are saved to {Config_File}.")

def show_config(config):
    print("\nCurrent preferences:")
    for key,value in config.items():
        print(f"{key}: {value}")

def update_config(config):
    key = input("\nEnter the preference you want to modify: ").strip()
    if key not in config:
        print(f"'{key}' does not exist in config.")
        return
    
    new_value = input(f"Enter new value for {key}: ").strip()

    if new_value == "":
        print("value cannot be empty.")
        return
    
    if key == "font size":
        try: 
            new_value = int(new_value)
        except ValueError:
            print("font size must be a number.")
            return

        if new_value < 8 or new_value > 32:
            print("font size is out of range (8 - 32).")
            return

    config[key] = new_value
    print("\nPreference updated successfully.")
    return config

def show_menu():
    print("\nMenu:")
    print("1. Show preferences")
    print("2. Modify preference")
    print("3. Save preferences")
    print("4. Exit")


config = read_config()

while True:
    #show_menu()
    print("\nMenu:")
    print("1. Show preferences")
    print("2. Modify preference")
    print("3. Save preferences")
    print("4. Exit")

    choice = input("Enter a choice: ").strip()

    if choice == "1":
        show_config(config)
    elif choice == "2":
        update_config(config)
    elif choice == "3":
        save_config(config)
    elif choice == "4":
        print("Exit.")
        break
    else:
        print("Invalid choice.")

