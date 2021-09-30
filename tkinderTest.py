'''
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


class Assistant_panel:

    assistant_list = {
     1 : QuickSortCatalogue ,
     2 : BubbleSortCatalogue ,
     3 : BucketSortCatalogue ,
     }

    def __init__(self, master):
       
        self.master = master
        master.title("Shop assistants to choose :")
        master.configure(background = "#006B38") #Setting the background color of Tk window
        master.geometry("900x300") #Width and height of Tk window

        # Open images
        self.assnt1 = Image.open("img/assistant1.jpg")
        self.assnt2 = Image.open("img/assistant2.jpg")
        self.assnt3 = Image.open("img/assistant3.jpg")

        # Resize images
        self.resize1 = self.assnt1.resize((300,225) , Image.ANTIALIAS)
        self.resize2 = self.assnt2.resize((300,225) , Image.ANTIALIAS)
        self.resize3 = self.assnt3.resize((300,225) , Image.ANTIALIAS)

        # Tkinter expects an image object so the ImageTk module contains support 
        # to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.
        #We use the PhotoImage which is A Tkinter-compatible photo image.
        self.assistant1 = ImageTk.PhotoImage(self.resize1)
        self.assistant2 = ImageTk.PhotoImage(self.resize2)
        self.assistant3 = ImageTk.PhotoImage(self.resize3)

        #Placing the ImmageTK.PhotoImage into a Label and then setting the location
        #inside Tk window
        self.my_label1 = Label(master , image = self.assistant1).grid(row=1 , column= 0, columnspan= 1)
        self.my_label2 = Label(master , image = self.assistant2).grid(row=1 , column= 1, columnspan= 1)
        self.my_label3 = Label(master , image = self.assistant3).grid(row=1 , column= 2, columnspan= 1)

        #Setting buttons bellow images for user to choose and their locations
        self.quick_sort_button  = Button(master , text = "Ms QuickSort"  , bg = "#101820" ,
                                         fg = "#FFFFFF" , command = lambda:self.button1(1)).grid(row = 2 , column = 0)
        self.bubble_sort_button = Button(master , text = "Mr BubbleSort" , bg = "#101820" ,
                                         fg = "#FFFFFF" , command = lambda:self.button1(2)).grid(row = 2 , column = 1)
        self.bucket_sort_button = Button(master , text = "Ms BucketSort" , bg = "#101820" , 
                                         fg = "#FFFFFF" , command = lambda:self.button1(3)).grid(row = 2 , column = 2)
        self.exit_main          = Button(master , text = "EXIT"          , bg = "#101820" ,
                                         fg = "red"     , command = lambda:self.exit_to_main(1)).grid(row = 3 , column = 1)

    
        
    
    def set_catalogues(self , assistant = None):
        if assistant:
            #print(assistant)
            self.master.geometry("900x500")
            
            # Open images
            self.cata1 = Image.open("img/cata1.jpg")
            self.cata2 = Image.open("img/cata2.jpg")

            # Resize images
            self.resize1 = self.cata1.resize((300,225) , Image.ANTIALIAS)
            self.resize2 = self.cata2.resize((300,225) , Image.ANTIALIAS)

            self.catalogue1 = ImageTk.PhotoImage(self.resize1)
            self.catalogue2 = ImageTk.PhotoImage(self.resize2)

            self.cata_label1 = Label(self.master , image = self.catalogue1)
            self.cata_label2 = Label(self.master , image = self.catalogue2)

            self.cata_label1.grid(row=0 , column= 2, columnspan= 1)
            self.cata_label2.grid(row=0 , column= 3, columnspan= 1)

            self.asc_color_button   = Button(self.master , text = "Ascending Color"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(1 , assistant))
            self.desc_color_button  = Button(self.master , text = "Descending Color"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(2 , assistant))
            self.asc_size_button    = Button(self.master , text = "Ascending Size"    , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(3 , assistant))
            self.desc_size_button   = Button(self.master , text = "Descending Size"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(4 , assistant))
            self.asc_fabric_button  = Button(self.master , text = "Ascending Fabric"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(5 , assistant))
            self.desc_fabric_button = Button(self.master , text = "Descending Fabric" , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(6 , assistant))
            self.asc_scf_button     = Button(self.master , text = "Ascending S-C-F"   , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(7 , assistant))
            self.desc_scf_button    = Button(self.master , text = "Descending S-C-F"  , bg = "#101820" , fg = "#FFFFFF" , command = lambda:self.button2(8 , assistant))
            self.exit               = Button(self.master , text = "EXIT"              , bg = "#101820" , fg = "red"     , command = lambda:self.exit_button(1))

            self.asc_color_button.grid(  row = 1 , column = 2 , sticky = "nsew")
            self.desc_color_button.grid( row = 1 , column = 3 , sticky = "nsew")
            self.asc_size_button.grid(   row = 2 , column = 2 , sticky = "nsew")
            self.desc_size_button.grid(  row = 2 , column = 3 , sticky = "nsew")
            self.asc_fabric_button.grid( row = 3 , column = 2 , sticky = "nsew")
            self.desc_fabric_button.grid(row = 3 , column = 3 , sticky = "nsew")
            self.asc_scf_button.grid(    row = 1 , column = 0 , sticky = "nsew")
            self.desc_scf_button.grid(   row = 2 , column = 0 , sticky = "nsew")
            self.exit.grid(              row = 3 , column = 0 , sticky = "nsew")


    def button1(self , x):
        if x == 1 :
            self.my_label2.destroy()
            self.my_label3.destroy()
            self.my_label1.grid(row = 0 , column = 0)
            self.exit_main.destroy()
            self.quick_sort_button.destroy()
            self.bubble_sort_button.destroy()
            self.bucket_sort_button.destroy()
            self.master.title("Ms QuickSort")
            self.strat_method = (Assistant_panel.assistant_list[x])()
            self.set_catalogues(self.strat_method)
        
        
        elif x == 2 :
            self.my_label1.destroy()
            self.my_label3.destroy()
            self.my_label2.grid(row = 0 , column = 0)
            self.exit_main.destroy()
            self.quick_sort_button.destroy()
            self.bubble_sort_button.destroy()
            self.bucket_sort_button.destroy()
            self.master.title("Mr BubbleSort")
            self.strat_method = (Assistant_panel.assistant_list[x])()
            self.set_catalogues(self.strat_method)

        else :
            self.my_label1.destroy()
            self.my_label2.destroy()
            self.my_label3.grid(row = 0 , column = 0)
            self.exit_main.destroy()
            self.quick_sort_button.destroy()
            self.bubble_sort_button.destroy()
            self.bucket_sort_button.destroy()
            self.master.title("Ms BucketSort")
            self.strat_method = (Assistant_panel.assistant_list[x])()
            self.set_catalogues(self.strat_method)


    def button2(self , x , assistant:CatalogueStrategy):
        if  x == 1 :
            sort_by = "asc"
            value = "color"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
                
        elif x == 2 :
            sort_by = "desc"
            value = "color"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)

        elif x == 3 :
            sort_by = "asc"
            value = "size"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
            
        elif x == 4 :
            sort_by = "desc"
            value = "size"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
        elif x == 5 :
            sort_by = "asc"
            value = "fabric"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
        elif x == 6 :
            sort_by = "desc"
            value = "fabric"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
        elif x == 7 :
            sort_by = "asc"
            value = "scf"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)
        elif x == 8 :
            sort_by = "desc"
            value = "scf"
            row = 4
            self.set_canvas(assistant , sort_by , value , row)


    def exit_button(self , e):
        if e:
            self.master.destroy()
            self.assistants_panel()

    def exit_to_main(self, e):
        if e:
            self.master.destroy()
           

    
    def set_canvas(self , assistant , sort_by , value , row):
        self.summer_catalogue = self.create_catalogue()
        self.cata_frame = Frame(self.master)
        self.cata_frame.grid(row = 4 , column = 2 , columnspan = 2 , sticky = "nsew")
        self.cata_canvas = Canvas(self.cata_frame)
        self.cata_canvas.pack(side = LEFT , fill = BOTH , expand = 1)
        self.scrollbar = Scrollbar(self.cata_frame , orient = VERTICAL , command = self.cata_canvas.yview)
        self.scrollbar.pack(side = RIGHT , fill = Y)
        self.cata_canvas.configure(yscrollcommand = self.scrollbar.set)
        self.cata_canvas.bind("<Configure>" , lambda e : self.cata_canvas.configure(scrollregion = self.cata_canvas.bbox("all")))
        self.second_frame = Frame(self.cata_canvas)
        self.cata_canvas.create_window((0 , 0) , window = self.second_frame , anchor = "nw")
        self.master.geometry("950x600")

        self.manage_assnt_ctlg = Assistants_Catalogue()
        self.manage_assnt_ctlg.showCatalogue(assistant , sort_by , value , self.summer_catalogue)

        for i in self.summer_catalogue :  
            row += 1
            TshirtCatalogue = Label(self.second_frame , text = i , bg = "#101820" , fg = "#FFFFFF" , anchor = "w" , font = "Helvetica")
            TshirtCatalogue.grid(row = row  , sticky = "nsew")













root = Tk()
my_gui = Assistant_panel(root)
root.mainloop()


'''