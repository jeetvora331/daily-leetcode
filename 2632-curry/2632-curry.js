/**
 * @param {Function} fn
 * @return {Function}
 */

// SOLUTION 1 ////////////////////////
// var curry = function(fn) {
//     return function curried() {
//         if (args.length > fn.length) {
//             return fn.apply(this , args)
//         }
//         return curried.bind(this , ...args)
//     };
// };

var curry = function(fn) {
   return function curried(...args) {
      if (args.length >= fn.length) {
          return fn(...args)
      }
        return (...nextArgs) => curried(...args , ...nextArgs)
   };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
