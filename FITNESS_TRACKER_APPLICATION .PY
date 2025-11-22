# Simple Fitness Tracker Application

def main_menu():
    print("\n=== Fitness Tracker ===")
    print("1. Log Steps")
    print("2. Log Calories")
    print("3. Log Water Intake")
    print("4. View Summary")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Initialize fitness data
fitness_data = {
    "steps": 0,
    "calories": 0,
    "water": 0.0  # in liters
}

while True:
    user_choice = main_menu()

    if user_choice == '1':
        steps = int(input("Enter steps walked today: "))
        fitness_data["steps"] += steps
        print(f"Total steps: {fitness_data['steps']}")

    elif user_choice == '2':
        calories = int(input("Enter calories consumed today: "))
        fitness_data["calories"] += calories
        print(f"Total calories: {fitness_data['calories']}")

    elif user_choice == '3':
        water = float(input("Enter water intake (liters): "))
        fitness_data["water"] += water
        print(f"Total water intake: {fitness_data['water']} L")

    elif user_choice == '4':
        print("\n=== Today's Fitness Summary ===")
        print(f"Steps walked: {fitness_data['steps']}")
        print(f"Calories consumed: {fitness_data['calories']}")
        print(f"Water intake: {fitness_data['water']} L")

    elif user_choice == '5':
        print("Exiting Fitness Tracker. Stay healthy!")
        break

    else:
        print("Invalid choice. Please try again.")
