def greatestNumber(array):
    steps = 0
    for i in array:
        steps +=1
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
        for j in array:
            steps +=1
        # If we find another value that is greater than i,
        # i is not the greatest:
            if j > i:
                isIValTheGreatest = False
                # If, by the time we checked all the other numbers, i
                # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i,steps
            

print("Algo 1 ",greatestNumber([1,2,3,4,5,29,2]))

#--------------------------------------------------
# Note: The above algo has timecomplexity of O(N^2)
# Lets Reduce to O(N)
#--------------------------------------------------

def greatestNum(array):
    steps = 0
    greatest_num  =  array[0]
    for i in array:
        steps +=1
        if i > greatest_num:
            greatest_num = i

    return greatest_num,steps

print("Algo 2 ",greatestNum([1,2,3,4,5,29,2]))




# Algo 2 is as twice as faster than algo 1 only 7 steps it take and Algo 1 take 48 steps