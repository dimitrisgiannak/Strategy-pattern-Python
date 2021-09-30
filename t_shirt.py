from stock import stock_color
from stock import stock_size
from stock import stock_fabric
from menu import menu , buy_more

from random import choice


t_shirts = list()  # List which will store all our T_Shirt objects

counter = 0  # Counter to show how many t-shirts picked

# A dictionary to get a random response when the client picks a t-shirt
responses = {
    1 : "That color enchances your eyes !! Great choice . " , 
    2 : "I think this size is the best for you " ,
    3 : "I REALLY admire customers with good taste ! Excellent choice ! " ,
    4 : "I have bought the same as a present for a dear friend. It is just too good ! " ,
    5 : "That was my first choice when i saw you wearing it ! " ,
    6 : "We can see many more but that one is the best for you !" ,
}

# Dictionary to help us sort size with a logical order
tShirtSize = {
"XS"   : 1 ,
"S"    : 2 ,
"M"    : 3 ,
"L"    : 4 ,
"XL"   : 5 ,
"XXL"  : 6 ,
"XXXL" : 7
}


class T_shirt:
    """
    Instantiate the object with the clients preferances using the class T_Shirt.
    """
    def __init__(self , color , size , fabric , cost):
        self.color  = color
        self.size   = size
        self.fabric = fabric
        self.cost   = cost

 
    def getter(self , value):
        '''
        We create a getter method to use when the value == "size".
        That is because we want to display XS S M L XL ...etc
        and not L M S XL XS XXL ...etc which would be the outcome if we
        sort the strings
        '''
        if value == "size":
            return tShirtSize[self.size]
        return getattr(self , value)

   
    def __str__(self):
        """
        Changing the output of the instance.
        """
        return (f"T shirt is {self.color} , with {self.size} size "
                f"and the fabric is {self.fabric}. "
                f"Total value is {self.cost} € "
                )


def buy_more_t_shirts(t_shirts):   
    """
    Method that gives the choice to create more t-shirts.
    If more == 1 then we get to create a new t-shirt and the old one
      is stored into t_shirts list.
    When more == 2 we return the list on our client method with the created t-shirts.
    If more is not 1 or 2 we respond in appropriate message.
    """
    while True:
        try:
            buy_more()  # Call's buy_more function to show the options the client got from menu.py
            more = int(input("Please choose : "))
            if more != 1 and more != 2 :
                raise ValueError
            break
        except ValueError:
            print("Please choose according to the numbers! \n")

    if more == 1 :
        print("Let's go through our choices again for you to pick : \n")
        tShirtCreate()  # Return's to previous method to construct another t-shirt
    else :
        print("Set and done!!! ")
    
    return t_shirts     # Return's the list of t-shirt into client.py



def tShirtCreate():
    """
    Method that helps the client to make a choice between the variations.
    It is used between the client and the context.
    When it's done we instantiate it using the class T_Shirt.
    The options about the variations are imported from module stock.py .
    In try except we check if the input is optimal according to our options
     and return an exception if it's not , with appropriate message. 
    """
    global counter
    menu()  # Call's menu function to show the options the client got from menu.py

    while True:
        try:
            t_shirt_dets = int(input("Please choose: "))

            # We convert int input to str and then creating a list of integers
            t_shirt_list = [int(a) for a in str(t_shirt_dets)] 

            # We have 3 categories to choose from so the len is always 3
            if len(t_shirt_list) != 3:  
                raise IndexError

            # We check if each individual choice is out of range regarding our options
            for i in t_shirt_list:
                if i > 7 or i < 1:  
                    raise ValueError
            break      
        except ValueError:
            print("You must give the appropriate numbers as shown in the table !\n")

        except IndexError: 
            """
            It's not actually an index error but it has the same meaning. We also changed exception to 
             output a different message.
            """
            print("You must choose between the three categories . "
                  "Your choice can only have three integers !!\n")
    
    # Changing to str in order to "break" the given number and use the indexes
    t_shirt_dets   = str(t_shirt_dets)
    t_shirt_color  = stock_color[t_shirt_dets[0]][0]
    t_shirt_size   = stock_size[t_shirt_dets[1]][0]
    t_shirt_fabric = stock_fabric[t_shirt_dets[2]][0]
    t_shirt_cost   = stock_color[t_shirt_dets[0]][1] + stock_size[t_shirt_dets[1]][1] + \
                     stock_fabric[t_shirt_dets[2]][1] 

    # Creating object with given details             
    t_shirt_create = T_shirt(
                            t_shirt_color ,
                            t_shirt_size ,    
                            t_shirt_fabric , 
                            t_shirt_cost   
                            )

    # Store object into the list.  
    t_shirts.append(t_shirt_create)  

    # Get a random response from the response dictionary
    print(choice(list(responses.values())) , "\n" * 2)  

    # Counter get's + 1 each time we pick a new t shirt
    counter += 1
    print(f"You have bought {counter} t-shirts \n")

    return buy_more_t_shirts(t_shirts)