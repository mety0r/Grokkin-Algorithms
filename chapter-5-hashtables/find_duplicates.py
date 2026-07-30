def find_duplicate(nums):
    # We first create a hash table
    seen = {}
    
    # We iterate through the list
    for num in nums:
        if num in seen:
            return num
        else:
            seen[num] = True
            
    return None

numbers = [3, 1, 4, 2, 5, 4, 6]

result = find_duplicate(numbers)
print(result)