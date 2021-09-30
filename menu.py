# This module contain's all the informations that the client needs
#in order to make a choice.
def opening_menu():
    print("\n")
    print("__        __   _                              ")
    print("\ \      / /__| | ___ ___  _ __ ___   ___     ")
    print(" \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \    ")
    print("  \ V  V /  __/ | (_| (_) | | | | | |  __/    ")
    print("   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|    ")
    print("                                              ")
    print("    /* Created by:                            ")
    print("            Dimitris Giannakopoulos           ")
    print("\n"*3)
    print("Hello and Welcome to our store!!\n\n\n")


def greetings():
    print("Would you like to buy something or go through our t-shirt catalogues ?")
    print("1 : Buy some t-shirts!!!\n2 : Go through your t-shirt catalogues\n3 : Just payed a visit!!Thank you")

  
def menu():
    print("Please choose one for each of the three variations for the T-Shirt you want to buy\n")
    print('''
            _________________________________________
           |    COLOR    |   SIZE    |    FABRIC     |
           |_____________|___________|_______________|
           | 1 : RED     |  1 : XS   | 1 : WOOL      |
           | 2 : ORANGE  |  2 : S    | 2 : COTTON    |
           | 3 : YELLOW  |  3 : M    | 3 : POLYESTER |
           | 4 : GREEN   |  4 : L    | 4 : RAYON     |
           | 5 : BLUE    |  5 : XL   | 5 : LINEN     |
           | 6 : INDIGO  |  6 : XXL  | 6 : CASHMERE  |
           | 7 : VIOLET  |  7 : XXXL | 7 : SILK      |
           |_____________|___________|_______________|

             Your choice should look like this : 123
             COLOR  : RED
             SIZE   : S
             FABRIC : POLYESTER

           If your choice is not according to this table you will be able 
           to choose again ..!
           Keep in mind that if you buy 3 or more t shirt you get a discount 
           of 15% !!!
    ''')   


def menu2():
   print("Please choose one for each of the three variations for the T-Shirt you want to buy\n")
   print('''
            _________________________________________
           |    COLOR    |   SIZE    |    FABRIC     |
           |_____________|___________|_______________|
           | 1 : RED     |  1 : XS   | 1 : WOOL      |
           | 2 : ORANGE  |  2 : S    | 2 : COTTON    |
           | 3 : YELLOW  |  3 : M    | 3 : POLYESTER |
           | 4 : GREEN   |  4 : L    | 4 : RAYON     |
           | 5 : BLUE    |  5 : XL   | 5 : LINEN     |
           | 6 : INDIGO  |  6 : XXL  | 6 : CASHMERE  |
           | 7 : VIOLET  |  7 : XXXL | 7 : SILK      |
           |_____________|___________|_______________|

             Your choice should look like this : 123
             COLOR  : RED
             SIZE   : S
             FABRIC : POLYESTE
        ''')


def buy_more():
  print("Would you like to buy another t_shirt? \n"
        "1 : Yes!!!\n2 : No thanks\n")


def payment_menu():
    print("And now that everything is set how would you like to pay?")
    print("We accept the following methods:\n")
    print('''
            PAYMENT METHODS
            1 : CREDIT/DEBIT CARDS
            2 : MONEY/BANK TRANSFER
            3 : CASH

          ''')
