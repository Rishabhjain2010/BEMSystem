#                                                                     by RishabhJain2010

#importing modules
# import sys
# sys.path.append("/SystemEngine/osessenstials.py")

# import osessenstials
from loginandregistration import register as registration
from loginandregistration import login 
from loginandregistration import elogin

def identityverification():

    loginopt = int(input("Please Enter 1 to login as Existing User! \nPlease Enter 2 for New Registration! \nPlease Enter 3 for Employee Login! \n "))
    # osessenstials.clear_terminal()
    #Login/Registration Window
    if loginopt == 1:
        return login.login()
    #Registration Form (Upload to host.py)
    elif loginopt == 2:
        return registration.registration()
    elif loginopt ==3:
        return elogin()
    elif loginopt!=1 | loginopt != 2 | loginopt != 3:
        print("Invalid Option!")
        return identityverification()