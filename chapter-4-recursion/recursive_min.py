def find_minimum(arr):
    if len(arr) == 1:
        return arr[0]   
    
    minimum_rest = find_minimum(arr[1:])
    
    if arr[0] < minimum_rest:
        return arr[0]
    return minimum_rest

print(find_minimum([5, 9, 1, 3, 7]))