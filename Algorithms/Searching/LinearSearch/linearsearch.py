def linearsearch(array, n):
    for index, x in enumerate(array):
        if x == n:
            return index, x
        elif x > n:
            break
    return -1

# Test the function
print(linearsearch([3, 5, 9, 10, 11, 16], 6))
