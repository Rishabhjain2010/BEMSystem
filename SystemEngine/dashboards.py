# Admin Dashboard

from osessenstials import clear_terminal
import time



def admin_dashboard(username):
    from root import mainmenu
    


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

            elif choice == 1:
                from event import new_event
                new_event(username)
            elif choice == 2:
                from event import delete_event
                delete_event(username)
            elif choice == 3:
                from accounts import view_sales
                view_sales()
            elif choice == 4:
                emp_managementdb(username)
            elif choice == 5:
                from event import view_event
                view_event(username)
            elif choice == 6:
                return  mainmenu()
            elif choice == 7:
                print("Logging out...")  # Placeholder for logout functionality
                break

        except ValueError:
            print("Invalid input. Please enter a number (1-7).")


### Employee Dashboard




def emp_dashboard(username):
    from root import mainmenu
    from createt_sale import new_sale 
    from event import view_event 
    from entry import verify_entry


    print("Welcome to the Employee Dashboard!")
    while True:
        print("\nPlease select an option:")
        print("1. Create New Sale")
        print("2. Verify Entry")
        print("3. View Live Events")
        print("4. Go back to main menu")
        print("5. Logout")

        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice not in range(1, 6):
                print("Invalid choice. Please try again.")
                continue

            elif choice == 1:
                new_sale(username)
            elif choice == 2:
                emp_id = input("Please Enter Your Employe ID: ")
                #view_sale(username , emp_id)
            elif choice == 3:
                admin_username = input("Please Enter Admin Username: ")
                view_event(admin_username)
            elif choice == 4:
                return mainmenu()
            elif choice == 5:
                print("Logging out...")
                break
            
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")

def emp_managementdb(username):
    from root import mainmenu
    clear_terminal()
    from employee import create_newemployee , delete_Emp , view_emp
    from root import mainmenu
    
    print("Welcome to the Employee Management Dashboard!")
    while True:
        print("\nPlease select an option:")
        print("1. Create New Employee")
        print("2. Delete Employee")
        print("3. View Employee")
        print("4. Go back to main menu")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice not in range(1, 5):
                print("Invalid choice. Please try again.")
                continue

            elif choice == 1:
                create_newemployee(username)
            elif choice == 2:
                delete_Emp(username)
            elif choice == 3:
                view_emp(username)
            elif choice == 4:
                return mainmenu()
          
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


#admin_dashboard("rishabhjain2010")
emp_dashboard("avstau")
