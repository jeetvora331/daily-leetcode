/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const cArr = []
    let index = 0
    
    while (index < arr.length){
        let count = size
        const temp = []
        
        while (count-- >0 && index<arr.length){
            temp.push(arr[index])
            index++
        }
        cArr.push(temp)
        
    }
    return cArr
};
