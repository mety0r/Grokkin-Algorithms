def sumofArr(arr, n):
    if n == 0:                                      
        return 0
    return arr [n - 1] + sumofArr(arr, n - 1)

n = int(input("Enter the number of elements in the array: "))
#Initialise array
arr = []
#for loop to store the values
for i in range(n):
    element = int(input(f"Enter the element:"))
    arr.append(element)
    
print("Array sum is: ", sumofArr(arr, n))  
