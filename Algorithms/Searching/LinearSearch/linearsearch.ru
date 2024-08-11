def linear_search(array, search_value)
    array.each_with_index do |element, index|
      if element == search_value
        return index
      elsif element > search_value
        break
      end
    end
    return -1
  end
  
  # Test the function
  p linear_search([1,2,3,4,5,6,7,8,9,10], 5)
  