#                                                                     by RishabhJain2010

#importing modules
import registration
import login
import elogin

def identityverification():

    loginopt = input("Please Enter 1 to login as Existing User! \nPlease Enter 2 for New Registration")
    
    #Login/Registration Window
    if loginopt == 1:
        return login.login()
    #Registration Form (Upload to host.py)
    elif loginopt == 2:
        return registration.registration()
    elif: loginopt ==3:
        return elogin()
    else:
        print("Invalid Option!")
        return identityverification()