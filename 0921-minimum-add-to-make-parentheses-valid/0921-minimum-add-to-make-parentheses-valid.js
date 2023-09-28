/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    while(s.indexOf("()") != -1) {
        s = s.replace("()", "");
    }
    return s.length;
    
};