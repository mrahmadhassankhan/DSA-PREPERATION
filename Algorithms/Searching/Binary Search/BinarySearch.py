def binarySearch(array, search_term):
    lowerBound = 0
    upperBound = len(array) - 1
    iterations = 0
    
    while lowerBound <= upperBound:
        iterations += 1   
        midpoint = (lowerBound + upperBound) // 2
        current_middle_value = array[midpoint]
        
        if search_term == current_middle_value:
            print(f"Number of iterations: {iterations}")
            return current_middle_value
        elif search_term < current_middle_value:
            upperBound = midpoint - 1
        else:
            lowerBound = midpoint + 1
    
    print(f"Number of iterations: {iterations}")
    return -1 

# Generate a large array from 1 to 99,999
large_array = list(range(1, 100000))

# Test the function
print(binarySearch(large_array, 73205))
