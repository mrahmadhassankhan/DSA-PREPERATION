function linearsearch(array, n) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] == n) {
      return i;
    }
  }
  return -1;
}

// Test the function
let result = linearsearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7);
console.log(result);
