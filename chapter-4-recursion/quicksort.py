#Quicksort Code

def quickSort(arr):
    
    #initialise a base case
    if len(arr) <= 1:
        return arr
    
    #Choose the first element as pivot 
    
    pivot = arr[0]
    
    #Create two empty list
    
    less = []
    greater = []
    
    #Then we compare the other element as pivot
    
    for i in range (1, len(arr)):
        if arr[i] <= pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])
            
    #recursively sort and combine 
    return quickSort(less) + [pivot] + quickSort(greater)

#main code
arr = [10, 5, 2, 3, 8, 1]
print(quickSort(arr))
    