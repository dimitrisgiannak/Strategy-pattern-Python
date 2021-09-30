import main
from strategy     import CatalogueStrategy
from strategy     import QuickSortCatalogue 
from strategy     import BubbleSortCatalogue
from strategy     import BucketSortCatalogue
from context      import Assistants_Catalogue 
from t_shirt      import T_shirt
from stock        import stock_color
from stock        import stock_size
from stock        import stock_fabric

from random       import randint

from tkinter      import *
from PIL          import ImageTk ,Image


# A dictionary with all available assistants
# Each str number is a Strategy class
assistant_list = {
     1 : QuickSortCatalogue ,
     2 : BubbleSortCatalogue ,
     3 : BucketSortCatalogue ,
     }


# Method that creates a t-shirt catalogue with clothes from class T_shirt
# Values taken from stock.py with existing dictionaries
# We store randint in separate value in order to find the total cost also
def create_catalogue():
    catalogue = []
    for i in range(40):
        ColorRand = str(randint(1 , 7))
        SizeRand = str(randint(1 , 7))
        FabricRand = str(randint(1 , 7))
        TshirtColor = stock_color[ColorRand][0]
        TshirtSize = stock_size[SizeRand][0]
        TshirtFabric = stock_fabric[FabricRand][0]
        TshirtCost = stock_color[ColorRand][1] + stock_size[SizeRand][1] + stock_fabric[FabricRand][1]

        TshirtDets = T_shirt(TshirtColor , TshirtSize , TshirtFabric , TshirtCost)
        catalogue.append(TshirtDets)
        
    return catalogue
    

# Accoring to the user's choice we change the Tk window to a more appropriate one
def button1(x):
    if x == 1 :
        my_label2.destroy()
        my_label3.destroy()
        my_label1.grid(row = 0 , column = 0)
        exit_main.destroy()
        quick_sort_button.destroy()
        bubble_sort_button.destroy()
        bucket_sort_button.destroy()
        assnt_display.title("Ms QuickSort")
        strat_method = (assistant_list[x])()  # Instanciating strategy method
        set_catalogues(strat_method)

    elif x == 2 :
        my_label1.destroy()
        my_label3.destroy()
        my_label2.grid(row = 0 , column = 0)
        exit_main.destroy()
        quick_sort_button.destroy()
        bubble_sort_button.destroy()
        bucket_sort_button.destroy()
        assnt_display.title("Mr BubbleSort")
        strat_method = (assistant_list[x])()
        set_catalogues(strat_method)

    else :
        my_label1.destroy()
        my_label2.destroy()
        my_label3.grid(row = 0 , column = 0)
        exit_main.destroy()
        quick_sort_button.destroy()
        bubble_sort_button.destroy()
        bucket_sort_button.destroy()
        assnt_display.title("Ms BucketSort")
        strat_method = (assistant_list[x])()
        set_catalogues(strat_method)




# Accoring to the user's choice we send the data to set_canvas() in order to create a canvas
def button2(x , assistant:CatalogueStrategy):
    if   x == 1 :
        sort_by = "asc"
        value = "color"
        row = 4
        set_canvas(assistant , sort_by , value , row)
            
    elif x == 2 :
        sort_by = "desc"
        value = "color"
        row = 4
        set_canvas(assistant , sort_by , value , row)

    elif x == 3 :
        sort_by = "asc"
        value = "size"
        row = 4
        set_canvas(assistant , sort_by , value , row)
        
    elif x == 4 :
        sort_by = "desc"
        value = "size"
        row = 4
        set_canvas(assistant , sort_by , value , row)
    elif x == 5 :
        sort_by = "asc"
        value = "fabric"
        row = 4
        set_canvas(assistant , sort_by , value , row)
    elif x == 6 :
        sort_by = "desc"
        value = "fabric"
        row = 4
        set_canvas(assistant , sort_by , value , row)
    elif x == 7 :
        sort_by = "asc_scf"
        value = "size"
        row = 4
        set_canvas(assistant , sort_by ,value , row)
    elif x == 8 :
        sort_by = "desc_scf"
        value = "size"
        row = 4
        set_canvas(assistant , sort_by , value , row)


# Clicking this button returns to the assistants_panel()
def exit_button(e):
    if e:
        assnt_display.destroy()
        assistants_panel()

# Clicking this button returns to the client_interaction() and we
#may choose again bettween catalogues and bying a t shirt
def exit_to_main(e):
    if e:
        assnt_display.destroy()
        main.client_interaction()


# We create a canvas inside Tk window and send the appropriate data to our contex
#class Assistants_Catalogue() to excecute the chosen strategy
def set_canvas(assistant:CatalogueStrategy , sort_by , value , row):
    summer_catalogue = create_catalogue()
    cata_frame = Frame(assnt_display)
    cata_frame.grid(row = 4 , column = 2 , columnspan = 2 , sticky = "nsew")
    cata_canvas = Canvas(cata_frame)
    cata_canvas.pack(side = LEFT , fill = BOTH , expand = 1)
    scrollbar = Scrollbar(cata_frame , orient = VERTICAL , command = cata_canvas.yview)
    scrollbar.pack(side = RIGHT , fill = Y)
    cata_canvas.configure(yscrollcommand = scrollbar.set)
    cata_canvas.bind("<Configure>" , lambda e : cata_canvas.configure(scrollregion = cata_canvas.bbox("all")))
    second_frame = Frame(cata_canvas)
    cata_canvas.create_window((0 , 0) , window = second_frame , anchor = "nw")
    assnt_display.geometry("950x600")

    manage_assnt_ctlg = Assistants_Catalogue()                                      # Creating an instance of our context class to handdle the sorting method
    manage_assnt_ctlg.showCatalogue(assistant , sort_by , value , summer_catalogue) 

    for i in summer_catalogue :                                                     # Our summer_catalogue returns sorted and we display each row inside canvas in a Label form
        row += 1
        TshirtCatalogue = Label(second_frame , text = i, bg = "#101820" , fg = "#FFFFFF" , anchor = "w" , font = "Helvetica")
        TshirtCatalogue.grid(row = row  , sticky = "nsew")



def set_catalogues(assistant = None): # assistant will be our strategy class
    if assistant:

        # Changing the size of our Tk window to meet our expectations
        assnt_display.geometry("900x500")
        
        # Open images
        cata1 = Image.open("img/cata1.jpg")
        cata2 = Image.open("img/cata2.jpg")

        # Resize images
        resize1 = cata1.resize((300,225) , Image.ANTIALIAS)
        resize2 = cata2.resize((300,225) , Image.ANTIALIAS)
        
        # The idea is the same as in assistants_panel()
        catalogue1 = ImageTk.PhotoImage(resize1)
        catalogue2 = ImageTk.PhotoImage(resize2)

        cata_label1 = Label(assnt_display , image = catalogue1)
        cata_label2 = Label(assnt_display , image = catalogue2)

        cata_label1.grid(row=0 , column= 2, columnspan= 1)
        cata_label2.grid(row=0 , column= 3, columnspan= 1)

        asc_color_button   = Button(assnt_display , text = "Ascending Color"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(1 , assistant))
        desc_color_button  = Button(assnt_display , text = "Descending Color"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(2 , assistant))
        asc_size_button    = Button(assnt_display , text = "Ascending Size"    , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(3 , assistant))
        desc_size_button   = Button(assnt_display , text = "Descending Size"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(4 , assistant))
        asc_fabric_button  = Button(assnt_display , text = "Ascending Fabric"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(5 , assistant))
        desc_fabric_button = Button(assnt_display , text = "Descending Fabric" , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(6 , assistant))
        asc_scf_button     = Button(assnt_display , text = "Ascending S-C-F"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(7 , assistant))
        desc_scf_button    = Button(assnt_display , text = "Descending S-C-F"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button2(8 , assistant))
        exit               = Button(assnt_display , text = "EXIT"              , bg = "#101820" , fg = "red"     , command = lambda:exit_button(1))

        asc_color_button.grid(  row = 1 , column = 2 , sticky = "nsew")
        desc_color_button.grid( row = 1 , column = 3 , sticky = "nsew")
        asc_size_button.grid(   row = 2 , column = 2 , sticky = "nsew")
        desc_size_button.grid(  row = 2 , column = 3 , sticky = "nsew")
        asc_fabric_button.grid( row = 3 , column = 2 , sticky = "nsew")
        desc_fabric_button.grid(row = 3 , column = 3 , sticky = "nsew")
        asc_scf_button.grid(    row = 1 , column = 0 , sticky = "nsew")
        desc_scf_button.grid(   row = 2 , column = 0 , sticky = "nsew")
        exit.grid(              row = 3 , column = 0 , sticky = "nsew")
        
        assnt_display.mainloop()  # Mainloop method is needed to keep our Tk window visible until we select to close it


# Creating the main window of our application with all the choices needed for the user to choose
def assistants_panel():  
    global my_label1 , my_label2 , my_label3
    global quick_sort_button , bubble_sort_button , bucket_sort_button , exit_main
    global assnt_display

    print("Please choose one of the following clothes assistants to help you\nin your search.\n\n")
   
    assnt_display = Tk()                               # Tk is the main window of an application
    assnt_display.title("Shop assistants to choose :") # Title of the Tk window
    assnt_display.configure(background = "#006B38")    # Setting the background color of Tk window
    assnt_display.geometry("900x300")                  # Width and height of Tk window

    # Open images
    assnt1 = Image.open("img/assistant1.jpg")
    assnt2 = Image.open("img/assistant2.jpg")
    assnt3 = Image.open("img/assistant3.jpg")

    # Resize images
    resize1 = assnt1.resize((300,225) , Image.ANTIALIAS)
    resize2 = assnt2.resize((300,225) , Image.ANTIALIAS)
    resize3 = assnt3.resize((300,225) , Image.ANTIALIAS)

    # Tkinter expects an image object so the ImageTk module contains support 
    #to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
    # We use the PhotoImage which is a Tkinter-compatible photo image
    assistant1 = ImageTk.PhotoImage(resize1)
    assistant2 = ImageTk.PhotoImage(resize2)
    assistant3 = ImageTk.PhotoImage(resize3)

    # Placing the ImmageTK.PhotoImage into a Label and then setting the location
    #inside Tk window
    my_label1 = Label(assnt_display , image = assistant1)
    my_label2 = Label(assnt_display , image = assistant2)
    my_label3 = Label(assnt_display , image = assistant3)

    my_label1.grid(row=1 , column= 0, columnspan= 1)
    my_label2.grid(row=1 , column= 1, columnspan= 1)
    my_label3.grid(row=1 , column= 2, columnspan= 1)

    # Setting buttons bellow images for user to choose and their locations
    quick_sort_button  = Button(assnt_display , text = "Ms QuickSort"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button1(1))
    bubble_sort_button = Button(assnt_display , text = "Mr BubbleSort" , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button1(2))
    bucket_sort_button = Button(assnt_display , text = "Ms BucketSort" , bg = "#101820" , fg = "#FFFFFF" , command = lambda:button1(3))
    exit_main          = Button(assnt_display , text = "EXIT"          , bg = "#101820" , fg = "red"     , command = lambda:exit_to_main(1))
    
    # We could do .grid above but we display them this way to be more understandable
    quick_sort_button.grid( row = 2 , column = 0)
    bubble_sort_button.grid(row = 2 , column = 1)
    bucket_sort_button.grid(row = 2 , column = 2)
    exit_main.grid(         row = 3 , column = 1)

    assnt_display.mainloop()  # Mainloop method is needed to keep our Tk window visible until we select to close it


        





























#assistants_panel()

