/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    acc = init 
    nums.forEach((ele) =>{
        acc = fn(acc,ele)
    })
    
    return acc
    
};