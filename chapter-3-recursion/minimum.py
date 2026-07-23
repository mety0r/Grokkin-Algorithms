#Maximum number using recursion

#define function
def minimum(arr, n):
    if n == 1:
        return arr[0]

    res = minimum(arr, n - 1)
    
    if arr[n - 1] < res:
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
    
print("The minimum element of the array is: ", minimum(arr, n))