#Sample Testing Process 
#Testing using pexpect

# Test Attempt: 1                                                                                                                                   
# Testing Date & Time: June 15 , 2024 (11:40 AM)

# Test Case 1 : 1) Redirecting to Admin User Login Page
#               2) Attempt Login
#               3) Redirecting to Admin Dashboard

# Given: 1) Login Credentials are Correct

# Expected Result: Test Case Passed
# Actual Result: Passed

#  ______________________________________________________________________________________________________________________________________________________________________

import pexpect

# Path to the script to be tested
path = '/home/rishabhjain2010/Repos/BEMSystem/BEMSystem/SystemEngine/root.py'

def test_case1():
    # Start the process using the Python interpreter
    child = pexpect.spawn(f'python3 {path}')
    
    # Redirecting to Admin User Login Page
    try:
        # Expecting the initial prompt
        child.expect('Please Enter 3 for Employee Login! ', timeout=100)
        # Sending input to select the admin login option
        child.sendline('1')
        print('Redirect to Admin User Login Page: Passed')
    except pexpect.TIMEOUT:
        print('Redirect to Admin User Login Page: Failed')
        return
    
    # Attempt Login
    try:
        # Expecting username prompt
        child.expect('Please Enter Username:', timeout=100)
        child.sendline('systemadmin')
        
        # Expecting password prompt
        child.expect('Please Enter Password:', timeout=100)
        child.sendline('admin@123')
        
        # Expecting welcome message
        child.expect('Welcome systemadmin', timeout=100)
        print('Login Attempt: Passed')
    except pexpect.TIMEOUT:
        print('Login Attempt: Failed')
        return

    # Redirecting to Admin Dashboard
    try:
        # Expecting admin dashboard welcome message
        child.expect('Welcome to the Admin Dashboard!', timeout=100)
        print('Redirect to Admin Dashboard: Passed')
    except pexpect.TIMEOUT:
        print('Redirect to Admin Dashboard: Failed')
        return
    
    # Redirecting to Admin Dashboard
    try:
        # Expecting admin dashboard welcome message
        child.expect('Welcome to the Admin Dashboard!', timeout=100)
        print('Redirect to Admin Dashboard: Passed')
    except pexpect.TIMEOUT:
        print('Redirect to Admin Dashboard: Failed')
        return
    
    print('Test Completed')

# Execute the test case
test_case1()
