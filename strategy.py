from abc import ABC , abstractmethod 

"""
 Strictly speaking this is not the classic Strategy pattern , meaning that each strategy class
should have only one strategy function.
 Taking a bit of creative freedom and because it still makes sence and works i just added more
strategy functions inside each class. Plus it adds more complication seperating them. For example :
CashStrategy into CashStrategyWithDisc and CashStrategyWithoutDisc.
"""

class PaymentMethodStrategy(ABC):
    """
     An interface that all Strategy subclasses/algorithms must implement.
     Abstract classes and methods have not an implementation.
    """ 
    @abstractmethod
    def payment_method_with_disc(self , x , y):
        pass

    @abstractmethod
    def payment_method(self , x , y):
        pass



class Credit_or_Debit_CardStrategy(PaymentMethodStrategy):
    """
     The subclass that implements an alternative algorithm.
     Same goes for the other subclasses.
     Our Strategy methods check if there is a discount also and accordingly
    proceed with the appropriate message. 
    """
    def payment_method_with_disc(self , discount , total_cost ):
        return "and you gonna pay with Credit / Debit card.\nBecause you bought enough t shirts you get a discount so\n" \
                f"total cost is : {total_cost}€\n" \
                f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"
 
    def payment_method(self , total_cost ):
        return "and you gonna pay with Credit / Debit card. " \
                f"Total cost is : {total_cost}€\n"



class Money_or_Bank_TransferStrategy(PaymentMethodStrategy):

    def payment_method_with_disc(self , discount , total_cost):  
        return "and you gonna pay with Money/Bank Transfer.\nBecause you bought enough t shirts you get a discount so\n" \
            f"total cost is : {total_cost}€\n" \
            f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"

    def payment_method(self , total_cost):  
        return "and you gonna pay with Money/Bank Transfer. " \
                f"Total cost is : {total_cost}€\n"


class CashStrategy(PaymentMethodStrategy):

    def payment_method_with_disc(self , discount , total_cost):     
        return "and you gonna pay with Cash.\nBecause you bought enough t shirts you get a discount so\n" \
                f"total cost is : {total_cost}€\n" \
                f"and after discount is : {total_cost - (total_cost * discount)}€ !!!\n"

    def payment_method(self , total_cost):
        return "and you gonna pay with Cash. " \
                f"Total cost is : {total_cost}€\n"



####################################################################################################################################

class CatalogueStrategy(ABC):
    """
     An interface that all Strategy subclasses/algorithms must implement.
     Abstract classes and methods have not an implementation.
    """ 
    @abstractmethod
    def asc(self , x , y):
        pass

    @abstractmethod
    def desc(self , x , y):
        pass

    @abstractmethod
    def asc_scf(self , x , y):
        pass

    @abstractmethod
    def desc_scf(self , x , y):
        pass


class QuickSortCatalogue(CatalogueStrategy):
    
    def asc(self , summer_cata , value):
        
        def partition(arr, low, high):
            i = (low-1)           # index of smaller element
            pivot = arr[high]     # pivot
        
            for j in range(low, high):
        
                # If current element is smaller than or
                # equal to pivot
                if arr[j].getter(value) <= pivot.getter(value):  # .getter(value) returns the object's attribute
                                                                 # If value == "size" it returns a number 
                    # increment index of smaller element
                    i = i + 1
                    arr[i], arr[j] = arr[j] , arr[i]
        
            arr[i+1] , arr[high] = arr[high] , arr[i+1]
            return (i + 1)
    
        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index
        
        # Function to do Quick sort 
    
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
        
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)
        
                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)
       
        return  quickSort(summer_cata, 0, len(summer_cata) - 1)


 
    def desc(self , summer_cata , value):
  
        def partition(arr, low, high):
            i = (low-1)         
            pivot = arr[high]    
        
            for j in range(low, high):
                if arr[j].getter(value) >= pivot.getter(value): # from ascending to descending we simply change the comparison operator
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
    
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
                pi = partition(arr, low, high)      
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)

        return  quickSort(summer_cata, 0, len(summer_cata) - 1)



    def asc_scf(self , summer_cata , value):

        def partition(arr, low, high):
            i = (low-1)         
            pivot = arr[high]     
            '''
             In this situation we want to compare the object in ascending by their size.
             If it's the same then we check their color and if it's the same again
            then we compare them according to the fabric attribute.
            '''
            if value == "size" :
                for j in range(low, high):       
                    if arr[j].getter(value) <= pivot.getter(value):
                        if arr[j].getter(value) < pivot.getter(value):
                            i = i + 1
                            arr[i] , arr[j] = arr[j] , arr[i]
                        
                        elif arr[j].getter(value) == pivot.getter(value):
                            if arr[j].color <= pivot.color:
                                if arr[j].color < pivot.color:
                                    i = i + 1
                                    arr[i] , arr[j] = arr[j] , arr[i]
                                                
                                elif arr[j].color == pivot.color:
                                    if arr[j].fabric < pivot.fabric :
                                        i = i + 1
                                        arr[i] , arr[j] = arr[j] , arr[i]
                                
            arr[i+1] , arr[high] = arr[high] , arr[i+1]
            return (i + 1)

        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:

                pi = partition(arr, low, high)

                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)
        
        return quickSort(summer_cata , 0 , len(summer_cata) - 1)


    def desc_scf(self , summer_cata , value):

        def partition(arr, low, high):
            i = (low-1)         
            pivot = arr[high]   
            '''
             In this situation we want to compare the object in descending by their size.
             If it's the same then we check their color and if it's the same again
            then we compare them according to the fabric attribute.
            '''  
            if value == "size" :
                for j in range(low, high):       
                    if arr[j].getter(value) >= pivot.getter(value): # from ascending to descending we simply change the comparison operator 
                        if arr[j].getter(value) > pivot.getter(value): # we check if > is True. if not we check if == is True.
                            i = i + 1                  # if == : then we check by object's attribute color etc...
                            arr[i] , arr[j] = arr[j] , arr[i]
                        
                        elif arr[j].getter(value) == pivot.getter(value):
                            if arr[j].color >= pivot.color:
                                if arr[j].color > pivot.color:
                                    i = i + 1
                                    arr[i] , arr[j] = arr[j] , arr[i]

                                elif arr[j].color == pivot.color:
                                    if arr[j].fabric > pivot.fabric :
                                        i = i + 1
                                        arr[i] , arr[j] = arr[j] , arr[i]
                                
            arr[i+1] , arr[high] = arr[high] , arr[i+1]
            return (i + 1)

        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:

                pi = partition(arr, low, high)

                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)

        return quickSort(summer_cata , 0 , len(summer_cata) - 1)


class BubbleSortCatalogue(CatalogueStrategy):

    def asc(self , summer_cata , value):
 
        def bubbleSort(arr):
            n = len(arr)
            
            # Traverse through all array elements
            for i in range(n):
  
            # Last i elements are already in place
                for j in range(0, n-i-1):
                  
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                    if arr[j].getter(value) > arr[j+1].getter(value) :
                        arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return bubbleSort(summer_cata)
    

    def desc(self , summer_cata , value):

        def bubbleSort(arr):
            n = len(arr)
    
            for i in range(n):
                for j in range(0, n-i-1):
                    if arr[j].getter(value) < arr[j+1].getter(value) :
                        arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return bubbleSort(summer_cata)


    def asc_scf(self , summer_cata , value):

        def bubbleSort(arr):
            n = len(arr)
            if value == "size":
                for i in range(n):
                    for j in range(0, n-i-1):

                        if arr[j].getter(value) != arr[j + 1].getter(value): 
                            if arr[j].getter(value) > arr[j+1].getter(value):
                                arr[j], arr[j+1] = arr[j+1], arr[j]
                        else:
                            if arr[j].color != arr[j + 1].color :
                                if arr[j].color > arr[j+1].color:
                                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                            else:
                                if arr[j].fabric > arr[j + 1].fabric :
                                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return bubbleSort(summer_cata)

    def desc_scf(self , summer_cata , value):

        def bubbleSort(arr):
            n = len(arr)
            if value == "size":
                for i in range(n):
                    for j in range(0, n-i-1):
            
                        if arr[j].getter(value) != arr[j + 1].getter(value) : 
                            if arr[j].getter(value) < arr[j+1].getter(value):
                                arr[j], arr[j+1] = arr[j+1], arr[j]
                        else:
                            if arr[j].color != arr[j + 1].color :
                                if arr[j].color < arr[j+1].color:
                                    arr[j], arr[j+1] = arr[j+1], arr[j]
                            else:
                                if arr[j].fabric < arr[j + 1].fabric :
                                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return bubbleSort(summer_cata)


    

'''
    We create a dictionary so each first letter of object's attribute has a number.We gave them floats.
    Inside bucket sort we turn floats to integers so int(0.1) == 0 , int(0.9) == 0 , int(2.3) == 2 etc.
    That way we create a bucket list with 3 buckets inside to sort. len(bucket) == 3 . Index 0 , 1 , 2. 
    We also created a second dictionary strictly used for bucket sort so when value == "size" we will 
    take the appropriate value from the key.
'''
num_dict = {
"A" : 0   , "B" : 0.1 , "C" : 0.2 , "D" : 0.3 , "E" : 0.4 , "F" : 0.5 , "G" : 0.6 , "H" : 0.7 ,
"I" : 0.8 , "J" : 0.9 , "K" : 1.0 , "L" : 1.1 , "M" : 1.2 , "N" : 1.3 , "O" : 1.4 , "P" : 1.5 ,
"Q" : 1.6 , "R" : 1.7 , "S" : 1.8 , "T" : 1.9 , "U" : 2.0 , "V" : 2.1 , "W" : 2.2 , "X" : 2.3 ,
"Y" : 2.4 , "Z" : 2.5    
    }

size_num = {
    1 : 0 , 2 : 0.1 , 3 : 0.2 , 4 : 1 , 5 : 1.1 , 6 : 1.2 , 7 : 1.3
}


class BucketSortCatalogue(CatalogueStrategy):

    def asc(self , summer_cata , value):
 
        def bucketSort(array):
            bucket = []

            # Create empty buckets
            for i in range(3):
                bucket.append([])

            # Insert elements into their respective buckets
            for j in array:   
                if value == "size":
                    index_b = int(size_num[j.getter(value)] )
                    bucket[index_b].append(j)
                else:       
                    index_b =  int(num_dict[j.getter(value)[0]])
                    bucket[index_b].append(j)
                
            # Sort the elements of each bucket
            for i in range(len(bucket)):
                bucket[i] = sorted(bucket[i] , key = lambda x : x.getter(value) , reverse = False)

            # Get the sorted elements
            k = 0
            for i in bucket:
                for j in i:
                    array[k] = j
                    k += 1
            return array
        
        return bucketSort(summer_cata)


  

    def desc(self , summer_cata , value):
        def bucketSort(array):
            bucket = []

            for i in range(3):
                bucket.append([])

            for j in array:   
                if value == "size": 
                    index_b = int(size_num[j.getter(value)] )
                    bucket[index_b].append(j)
                else:
                    index_b =  int(num_dict[j.getter(value)[0]])
                    bucket[index_b].append(j)
                
            for i in range(len(bucket)):
                bucket[i] = sorted(bucket[i] , key = lambda x : x.getter(value) , reverse = True)

            k = 0
            for i in bucket[::-1]:
                for j in i:
                    array[k] = j
                    k += 1
            return array
        
        return bucketSort(summer_cata)


    def asc_scf(self , summer_cata , value):

        def bucketSort(array):
            bucket = []

            # Create empty buckets
            for i in range(3):
                bucket.append([])

            # Insert elements into their respective buckets
            for j in array:      
                if value == "size": 
                    index_b = int(size_num[j.getter(value)] )
                    bucket[index_b].append(j) 
          
            # Sort the elements of each bucket
            for i in range(len(bucket)):
                bucket[i] = sorted(bucket[i] , key = lambda x : (size_num[x.getter(value)] , x.color , x.fabric)  , reverse = False)

            # Get the sorted elements
            k = 0
            for i in bucket:
                for j in i:
                    array[k] = j
                    k += 1
            return array
        
        return bucketSort(summer_cata)


    def desc_scf(self , summer_cata , value):
        def bucketSort(array):
            bucket = []

            # Create empty buckets
            for i in range(3):
                bucket.append([])

            # Insert elements into their respective buckets
            for j in array:            
                if value == "size": 
                    index_b = int(size_num[j.getter(value)] )
                    bucket[index_b].append(j)
                
            # Sort the elements of each bucket and reverse them
            for i in range(len(bucket)):
                bucket[i] = sorted(bucket[i] , key = lambda x : (size_num[x.getter(value)] , x.color , x.fabric)  , reverse = True)

            # Get the sorted elements starting from the last bucket
            k = 0
            for i in bucket[::-1]:
                for j in i:
                    array[k] = j
                    k += 1
            return array
        
        return bucketSort(summer_cata)