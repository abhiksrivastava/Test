def two_sum(nums, target):
    # Create a dictionary to store the difference and its index
    num_map = {}
    
    for index, num in enumerate(nums):
        # Calculate the difference needed to reach the target
        difference = target - num
        
        # Check if the difference is already in the map
        if difference in num_map:
            return [num_map[difference], index]
        
        # Store the index of the current number
        num_map[num] = index
    
    # If no solution is found, return None
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
