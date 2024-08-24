def bubble_sort(array)
  unsorted_last_index = array.length - 1
  sorted = false
  for i in 0...unsorted_last_index
    sorted = true
    for j in 0...(unsorted_last_index - i)
      if array[j] > array[j + 1]
        array[j], array[j + 1] = array[j + 1], array[j]
        sorted = false
      end
    end
    break if sorted
  end
end

array = [12, 3, 4, 5, 64, 12, 4, 11, 2]
bubble_sort(array)
puts "Sorted Array: #{array}"
