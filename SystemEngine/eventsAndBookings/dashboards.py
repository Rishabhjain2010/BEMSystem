# Admin Dashboard

from eventsAndBookings import event


def admin_dashboard():
    print("Welcome to the Admin Dashboard!")
    while True:
        print("\nPlease select an option:")
        print("1. Create New Event")
        print("2. Delete Event")
        print("3. View Sales")
        print("4. Manage Employee")
        print("5. View Live Events")
        print("6. Go back to main menu")
        print("7. Logout")

        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice not in range(1, 8):
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                event.new_event()
            elif choice == 2:
                delete_event()
            elif choice == 3:
                delete_event()
            elif choice == 4:
                manage_employee()
            elif choice == 5:
                view_live_events()
            elif choice == 6:
                return  # Return to the main menu
            elif choice == 7:
                print("Logging out...")  # Placeholder for logout functionality
                break

        except ValueError:
            print("Invalid input. Please enter a number (1-7).")

def create_new_event():
    print("Creating a new event...")
    new_event()
   

def view_sales():
    print("Viewing sales...")
    # Implement view sales logic here

def delete_event():
    print("Deleting an event...")
    # Implement event deletion logic here

def manage_employee():
    print("Managing employees...")
    # Implement employee management logic here

def view_live_events():
    print("Viewing live events...")
    # Implement live events viewing logic here

