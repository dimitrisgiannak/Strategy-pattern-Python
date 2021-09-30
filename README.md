# Strategy-pattern-Python

Coding Bootcamp assignment 4

* Following assignment 3 we are required to do a comparative analysis where we need to implement three sorting algorithms:
   1.Quick Sort
   2.Bubble Sort
   3.BucketSort


* We need to create at least forty T-shirts with random variations 
* On purpose each time we want to sort the list we create a new list 
   with 40 T-shirts just to have different samples
* Using the above algorithms we need to sort : 
   1.Size in ascending
   2.Size in descending
   3.Color in ascending
   4.Color in descending
   5.Fabric in ascending
   6.Fabric in descending
   7.Size and Color and Fabric in ascending
   8.Size and Color and Fabric in descending

* I use Strategy pattern like assignment 3 and the Strategy concrete classes
   are the sorting algorithms.
* When you first excecute the project in the intro menu you get the choice to 
   access assignment 3( 1rst option) ,
          assignment 4( 2nd option) ,
          leave the shop (close the project , 3rd option)
* Instead of using the console to output the user's choices i used Tkinder 
   which is Python's build-in library and standard interface to the Tcl/Tk GUI toolkit
   (No need to pip install)
* Once you select the 2nd option on intro menu the Tk window will pop up and from there 
   you choose with which algorithm you want to sort the T-shirt list
* You can run all three sorting algorithms without closing the project
* You can exit and come back to intro menu where you can start from the very beggining
   and make your choices again
* Strategy pattern needs to have a single concrete class with a single strategy method inside
   to excecute.
   As i explain in the strategy.py file i used a concrete class (BucketSortCatalogue) with 
   all the required strategy methods inside to solve the given task. This way i did not had to
   create many more classes with almost same names just to perform a single strategy method
   
* To start the project you need to run the main.py file
