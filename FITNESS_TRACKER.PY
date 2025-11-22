import time
from datetime import datetime

# --- Data Structure ---
# List to hold all logged activities. Each activity is a dictionary.
activity_log = []

def log_activity(activity_type, duration_minutes, distance_km=0):
    """Logs a new activity entry."""
    try:
        duration = float(duration_minutes)
        distance = float(distance_km)
    except ValueError:
        print("Error: Duration and distance must be numbers.")
        return

    # Create a unique entry for the activity
    entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'type': activity_type.lower(),
        'duration_min': duration,
        'distance_km': distance
    }

    activity_log.append(entry)
    print(f"\n✅ Logged: {activity_type.capitalize()} for {duration} minutes (Distance: {distance} km).")

def view_summary():
    """Calculates and displays a summary of all logged activities."""
    if not activity_log:
        print("\n😔 No activities logged yet.")
        return

    total_duration = 0
    total_distance = 0
    activity_counts = {}

    for activity in activity_log:
        total_duration += activity['duration_min']
        total_distance += activity['distance_km']

        activity_type = activity['type']
        activity_counts[activity_type] = activity_counts.get(activity_type, 0) + 1

    print("\n====================================")
    print("       FITNESS TRACKER SUMMARY      ")
    print("====================================")
    print(f"Total Activities Logged: {len(activity_log)}")
    print(f"Total Exercise Time:     {total_duration:.2f} minutes")
    print(f"Total Distance Covered:  {total_distance:.2f} km")
    print("--- Breakdown by Activity Type ---")
    for activity, count in activity_counts.items():
        print(f"- {activity.capitalize()}: {count} times")
    print("====================================\n")


def display_menu():
    """Displays the main menu options."""
    print("\n--- Fitness Tracker Menu ---")
    print("1. Log New Activity")
    print("2. View Summary")
    print("3. View Detailed Log")
    print("4. Exit")

def main():
    """Main function to run the application loop."""
    print("Welcome to the Simple Fitness Tracker!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\n--- Log Activity ---")
            activity = input("Enter activity type (e.g., Run, Walk, Lift): ")
            duration = input("Enter duration in minutes: ")
            distance = input("Enter distance in km (enter 0 if not applicable): ")
            log_activity(activity, duration, distance)

        elif choice == '2':
            view_summary()

        elif choice == '3':
            print("\n--- Detailed Activity Log ---")
            if not activity_log:
                print("No activities logged yet.")
            else:
                for idx, entry in enumerate(activity_log):
                    print(f"#{idx+1} | {entry['timestamp']} | Type: {entry['type'].capitalize()}")
                    print(f"    Duration: {entry['duration_min']} min | Distance: {entry['distance_km']} km")
            print("-----------------------------\n")

        elif choice == '4':
            print("👋 Thank you for using the tracker. Goodbye!")
            break

        else:
            print("\n❗ Invalid choice. Please enter a number between 1 and 4.")
            # Simple pause to make the output readable
            time.sleep(1) 

if _name_ == "_main_":
    main()
