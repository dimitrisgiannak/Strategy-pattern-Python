import assistants
from purchase import *
from menu import opening_menu , greetings
import sys


def client_interaction():
    '''
     Helper method to let user to choose between bying a t-shirt 
     or looking at the sorted catalogues
    '''
    cust_choice = None
    greetings()                        # menu.py --> greetings()
    while True:
        customer_choice_list = ["1" , "2" , "3"]
        try:
            cust_choice = int(input("Please reply:\n"))
            cust_choice = str( cust_choice)
            if len(cust_choice) != 1:  # Choice is len == 1 always
                raise IndexError
            if  cust_choice not in customer_choice_list:
                raise ValueError
            break
        except ValueError:
            print("You must give the appropriate reply as shown in the choices !")
        except IndexError:
            print("You must choose between the three choices . "
                  "Your choice can't have more than one number !!")
    if cust_choice == "1":
        taking_order()                  # purchase.py --> taking_order()
    elif cust_choice == "2":
        assistants.assistants_panel()   # assistants.py --> assistants_panel()
    else:
        print("Thank you for visiting us. Have a nice day!!")
        sys.exit(0)





if __name__ == "__main__":               # this is where our programm begins
    opening_menu()
    client_interaction()
    
    



