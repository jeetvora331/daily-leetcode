/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
const helper=(key,value) => {
    if (value && typeof value ==="object" && !Array.isArray(value)){
        
            return Object.fromEntries(Object.entries(value).sort())
    
        
    }
    else {
            return value
        }
    
}


var areDeeplyEqual = function(o1,o2){
    const s1 = JSON.stringify(o1,helper)
    const s2 = JSON.stringify(o2,helper)
    
    return s1 === s2
}