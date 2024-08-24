def bubble_sort(list):
    unsorted_until_index = len(list)-1  #Track Rightmost index that is not sorted yet
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i]> list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                sorted = False
        unsorted_until_index -=1
    return list


print(bubble_sort([65,45,11,23,999,34,1,3]))
