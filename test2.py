from test import create_catalogue
#from context import Assistants_Catalogue
#from strategy import QuickSortCatalogue
'''
array = create_catalogue()

#QUICKSORT

class QuickSortCatalogue():
    def desc_color(self , cata):
        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
        
            for j in range(low, high):
                if arr[j].color >= pivot.color:
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

        n = len(cata)
        return quickSort(cata , 0 ,n-1)

    def asc_color(self , cata):
        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
        
            for j in range(low, high):
                if arr[j].color <= pivot.color:
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

        n = len(cata)
        return quickSort(cata , 0 ,n-1)

class Assistants_Catalogue:

    @staticmethod
    def showCatalogue_asc(sorting_pattern , sort_by , value , summer_catalogue):
        if sort_by == "asc" and value == "color":
            return sorting_pattern.asc_color(summer_catalogue)

        if sort_by == "desc" and value == "color":
            return sorting_pattern.desc_color(summer_catalogue)
    


arr = array
a = QuickSortCatalogue()
manage_assnt_ctlg = Assistants_Catalogue()
z = manage_assnt_ctlg.showCatalogue_asc(a, "asc" , "color" , array)
for i in z:
    print(i)


def start():
    arr = array
    n = len(arr)
    b = QuickSortCatalogue()
    c = Assistants_Catalogue()
    d = c.showCatalogue_asc(b , "desc" , "color" , arr)

    print("Sorted array is:")
    for i in arr:
        print(i)

start()

#BUBBLESORT

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Driver code to test above
arr = ["a", "q", "z", "d", "e", "e","w", "c"]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i]) 


#BUCKETSORT

num_dict = {
    "A" : 0 , "B" : 0.1 , "C" : 0.2 , "D" : 0.3 , "E" : 0.4 , "F" : 0.5 , "G" : 0.6 , "H" : 0.7 ,
    "I" : 0.8 , "J" : 0.9 , "K" : 1.0, "L" : 1.1, "M" : 1.2, "N" : 1.3, "O" : 1.4, "P" : 1.5,
    "Q" : 1.6, "R" : 1.7, "S" : 1.8, "T" : 1.9, "U" : 2.0, "V" : 2.1, "W" : 2.2, "X" : 2.3,
    "Y" : 2.4, "Z" : 2.5    
}

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(3):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        
        index_b =  int(num_dict[j.color[0]])
        bucket[index_b].append(j)
        

    # Sort the elements of each bucket
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i] , key = lambda x : x.color , reverse = False)

    # Get the sorted elements
    k = 0
    for i in bucket:
        for j in i:
            array[k] = j
            k += 1
    return array

# Driver Code

array = create_catalogue()
#x = [12,32,54,1,435,2]
#x = [0.897, 0.565, 0.656,
#	0.1234, 0.665, 0.3434]
print("Sorted Array is")
bucketSort(array)
for i in array:
    print(i)

#print(bucketSort(x))




#BUBBLESORT asc taking all object's attributes into account

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
  
        for j in range(0, n-i-1):
  
            if arr[j].size != arr[j + 1].size : 
                if arr[j].size < arr[j+1].size:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j].color != arr[j + 1].color :
                    if arr[j].color < arr[j+1].color:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                
                else:
                    if arr[j].fabric < arr[j + 1].fabric :
                        arr[j], arr[j+1] = arr[j+1], arr[j]

  
# Driver code to test above
arr = create_catalogue()
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i]) 


#QUICKSORT DESCENDING SIZE COLOR FABRIC


def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     

    for j in range(low, high):       
        if arr[j].size >= pivot.size:
            if arr[j].size > pivot.size:
                i = i + 1
                arr[i] , arr[j] = arr[j] , arr[i]
             
            elif arr[j].size == pivot.size:
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

arr = create_catalogue()
quickSort(arr , 0 , len(arr) - 1)

for i in arr:
    print(i)

#BUCKETSORT DESCENDING SIZE COLOR FABRIC

num_dict = {
    "A" : 0 , "B" : 0.1 , "C" : 0.2 , "D" : 0.3 , "E" : 0.4 , "F" : 0.5 , "G" : 0.6 , "H" : 0.7 ,
    "I" : 0.8 , "J" : 0.9 , "K" : 1.0, "L" : 1.1, "M" : 1.2, "N" : 1.3, "O" : 1.4, "P" : 1.5,
    "Q" : 1.6, "R" : 1.7, "S" : 1.8, "T" : 1.9, "U" : 2.0, "V" : 2.1, "W" : 2.2, "X" : 2.3,
    "Y" : 2.4, "Z" : 2.5    
}

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(3):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:            
        index_b =  int(num_dict[j.size[0]])
        bucket[index_b].append(j)
        
    # Sort the elements of each bucket
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i] , key = lambda x : (x.size , x.color , x.fabric)  , reverse = False)

    # Get the sorted elements
    k = 0
    for i in bucket:
        for j in i:
            array[k] = j
            k += 1
    return array.reverse()

# Driver Code

array = create_catalogue()
#x = [12,32,54,1,435,2]
#x = [0.897, 0.565, 0.656,
#	0.1234, 0.665, 0.3434]
print("Sorted Array is")
bucketSort(array)
for i in array:
    print(i)

#print(bucketSort(x))

'''