from strategy import CashStrategy 
from strategy import Credit_or_Debit_CardStrategy
from strategy import Money_or_Bank_TransferStrategy
from menu import payment_menu

#A dictionary with all available payment methods.
#Each str number is a Strategy
accepted_payment_methods = {
     "1" : Credit_or_Debit_CardStrategy ,
     "2" : Money_or_Bank_TransferStrategy ,
     "3" : CashStrategy ,
}


def paymentMethod():
    """
    Function that helps the client pick the strategy he wants.
    In try except we check if the option he gave is valid.
    If not , respond with appropriate message.
    """
    payment_menu()                       #Call's function to show the options of payment from menu.py
    while True:
        payment_list = ["1" , "2" , "3"]
        try:
            payment_method = int(input("Please choose: "))
            payment_method = str(payment_method)
            if len(payment_method) != 1:  #Choise is len == 1 always
                raise IndexError
            if payment_method not in payment_list:
                raise ValueError
            break
        except ValueError:
            print("You must give the appropriate number as shown in the table !")
        except IndexError:
            print("You must choose between the three payment methods. "
                  "Your choice can't have more than one number !!")

    #We use the dictionary with our options and instantiate it using () at the end.
    return (accepted_payment_methods[payment_method])()