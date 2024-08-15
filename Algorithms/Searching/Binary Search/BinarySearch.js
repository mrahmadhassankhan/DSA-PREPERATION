function binarySearch(arr,number,lowerbound,upperbound){
    while (lowerbound<=upperbound){
  let middlepoint = Math.floor((lowerbound+upperbound)/2);
        if(number === arr[middlepoint]){
            return middlepoint;
        }
        else if (arr[middlepoint]< number){
           lowerbound =  middlepoint +1;
        }
        else {
            upperbound = middlepoint -1;
        }
}
return -1;
}
let numbers = [1,2,3,4,5,6,7,8,9]
console.log(binarySearch(numbers,8,0,numbers.length-1));


