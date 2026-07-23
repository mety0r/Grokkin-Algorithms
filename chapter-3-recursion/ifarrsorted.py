# define if sorted function  with two parameters array and the length of the arr

def isSorted(arr, n):
    if n == 1:
        return True
    
    if arr[n - 2] > arr[n - 1]:
        return False
    
    return isSorted(arr, n - 1)

n = int(input("Enter the number of elements: "))

#initialise new array
arr = []

#initialise loop to store elements
for i in range(n):
    arr.append(int(input("Enter the elements for array: ")))
 
# Condition to check if sorted    
if isSorted(arr, n):
    print("Arr is sorted")
else:
    print("Arr is not Sorted")
    
