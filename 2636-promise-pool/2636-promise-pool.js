/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    const eval = async() =>{
        if (functions.length === 0) return 
    
        const currentFunction = functions.shift()
        await currentFunction()
        await eval()
    } 
    
    const nPromises = Array(n).fill().map(eval)
    await Promise.all(nPromises)

};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */