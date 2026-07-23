#Maximum number using recursion

#define function
def maximum(arr, n):
    if n == 1:
        return arr[0]

    res = maximum(arr, n - 1)
    
    if arr[n - 1] > res:
        return arr[n - 1]
    else:
        return res
    
#Prompt user to enter elements
n = int(input("Enter the number of elements: "))

#initialise new arr
arr = []

#initialise loop to store elements
for i in range(n):
    arr.append(int(input("Enter the elements for array: ")))
    
print("The maximum element of the array is: ", maximum(arr, n))