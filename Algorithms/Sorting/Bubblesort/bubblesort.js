function bubble_sort(array){
   let unsorted_last_index = array.length -1
    let sorted = false
    for (let i=0;i<unsorted_last_index;++i){
        sorted = true
        for(let j=0;j<unsorted_last_index-i;++j){
            if(array[j]>array[j+1]){
                [array[j],array[j+1]] =[array[j+1],array[j]]
                sorted = false
            }
        }
        if (sorted)break;
    }
}


let array = [13,88,91,22,1,23,12,3]
bubble_sort(array)
console.log("Sorted Array:",array)