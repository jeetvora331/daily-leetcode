/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (
        obj === null || obj === undefined || typeof classFunction !== "function"
    ) {
        return false
    }
    
    let temp = Object.getPrototypeOf(obj)
    while (temp !== null){
        if (temp == classFunction.prototype) return true 
    else{
        temp = Object.getPrototypeOf(temp)
    }    
    }
    
    return false
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */