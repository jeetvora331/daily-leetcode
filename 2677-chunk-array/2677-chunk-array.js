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
        
        while (index<arr.length){
            cArr.push(arr.slice(index , index + size ))
            index = index + size     
        }
        
        
    }
    return cArr
};
