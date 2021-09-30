from payMethods import  paymentMethod
from t_shirt import  tShirtCreate
from context import ManagePayment

'''
 The taking_order function is responsible of making the t-shirts , paymentmethod
and ManagePayment and wrap them all up when the time comes.
'''

def taking_order():
    """
     The client picks the t-shirt/s of his choosing and after that picks
    a concrete strategy and passes it to the context.
     In our case the concrete strategies is the payment method with or without discount.
     The client has the choice to buy more than one t-shirts and can decide 
    the method to pay at the very end.
    """
    total_cost = 0                    # We will get the total cost of all t-shirts in the for loop
    t_shirt_created = tShirtCreate()  # This will be a list of objects with min len == 1
    payment = paymentMethod()         # Selecting the payment method (Strategy method)
    manage_payment = ManagePayment()  # Instantiating an object of context class to handdle payment
    """
     Using the len of the list because we want to output the strategy method
    on the clients last option rather than having it multiple times on the end.
     When the len of his choice list is 1 then we will output his method of payment(strategy method)
    and the discount if there is any. Getting discount will need at least 3 t-shirts.
    """
    if len(t_shirt_created) >= 3 :
        for i in range(len(t_shirt_created)) :
            total_cost += t_shirt_created[i].cost  # .cost is an instance attribute of object defined inside 
                                                   #the constructor of class T_Shirt

            if  len(t_shirt_created[i:]) == 1 :    # Inside for loop when the i == 1 then len == 1 so we display the payment method
                print(f"{i + 1} : {t_shirt_created[i]}" + "\n\n" + manage_payment.executePurchase(payment , 0.15 , total_cost ))
                    
            else:
                print(f"{i + 1} : {t_shirt_created[i]}")

    elif len(t_shirt_created) == 2 :               # We check the len == 2 because we need to display the total cost in the end with the payment method
         for i in range(len(t_shirt_created)) :    #but no discount
            total_cost += t_shirt_created[i].cost

            if  len(t_shirt_created[i:]) == 1 :  
                print(f"{i + 1} : {t_shirt_created[i]}" + "\n\n" + manage_payment.executePurchase(payment , None ,total_cost ))     

            else:
                print(f"{i + 1} : {t_shirt_created[i]}")

    else :
        total_cost = t_shirt_created[0].cost
        print(f"{1} : {t_shirt_created[0]}" + "\n\n" + manage_payment.executePurchase(payment , None , total_cost ))
    print()
    print("Thank you for your purchase . Please let us know if we can do anything else to help!\n\n")
  


