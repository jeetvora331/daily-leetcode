/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let res = []
    const flat = (nums , lvl) =>{
        for (const num of nums){
            if (Array.isArray(num) && lvl> 0){
                //rec call
                flat(num, lvl -1)
            }
            else{
                res.push(num)
            }
        }
    }
    flat(arr, n)
    return res
    
    
};