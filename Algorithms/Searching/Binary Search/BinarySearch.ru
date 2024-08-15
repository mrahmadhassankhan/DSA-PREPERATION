def binarySearch(arr, n)
    lowerbound = 0
    upperbound = arr.size - 1
  
    while lowerbound <= upperbound
      middlepoint = (lowerbound + upperbound) / 2
  
      if arr[middlepoint] == n
        return middlepoint
      elsif arr[middlepoint] < n
        lowerbound = middlepoint + 1
      else
        upperbound = middlepoint - 1
      end
    end
  
    return -1
  end
  
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  puts binarySearch(nums, 3) # Output: 2 (index of number 3 in the array)
  