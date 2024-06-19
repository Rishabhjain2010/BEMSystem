# Employee Management
from prettytable import PrettyTable
from dbconnect import dbconnect_employee
from dashboards import emp_managementdb
import time
from osessenstials import clear_terminal


def create_newemployee(username):
    clear_terminal()
    collection = dbconnect_employee()
    # company= username
    employeeID = input(" Enter Employee ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter last Namme: ")
    position = input("Enter Position: ")
    salary = float(input("Enter Salary: "))
    contact = input("Employee Contact: ")
    add_employee(collection , username , employeeID , first_name , last_name , position , salary , contact )
    add_another = input("To add another employee press Enter or any other Key to go back to Previous Menu")
    if (add_another == ""):
        create_newemployee(username)
    else:
        emp_managementdb(username)


    
    

def delete_Emp(username):
    clear_terminal()
    collection =dbconnect_employee()
    employee_id= input("Please Enter Employee ID: ")
    result = collection.delete_one({"employee_id": employee_id , "company" : username})
    if result.deleted_count == 1:
        print(f"Employee with ID {employee_id} deleted successfully.")
    else:
        print(f"No employee found with ID {employee_id}.")
    del_another = input("To Delete another employee press Enter or any other Key to go back to Previous Menu")
    if (del_another == ""):
        create_newemployee(username)
    else:
        emp_managementdb(username)


def view_emp(username):
    clear_terminal()
    collection = dbconnect_employee()
    employees = collection.find({"company": username})
    table = PrettyTable()
    table.field_names = ["Employee ID", "First Name", "Last Name", "Position", "Salary" , "Contact"]
    
    for employee in employees:
        table.add_row([employee['employee_id'], employee['first_name'], employee['last_name'], employee['position'], employee['salary'], employee['contact']])
    
    if table.rowcount == 0:
        print("No employees found associated with your company.")
    else:
        print(table)
    from dashboards import emp_managementdb
    input("Press Enter to go back to Previous Menu")
    emp_managementdb(username)


    


def add_employee(collection, username , employeeID  ,  first_name, last_name, position, salary , contact):
    employee = {
        "company": username,
        "employee_id" : employeeID  ,
        "first_name": first_name,
        "last_name": last_name,
        "position": position,
        "salary": salary,
        "contact": contact,
    }
    collection.insert_one(employee)
    print("Employee added successfully.")
    time.sleep(5)

# create_newemployee("systemadmin")
# view_emp("systemadmin")
# delete_Emp('systemadmin')
