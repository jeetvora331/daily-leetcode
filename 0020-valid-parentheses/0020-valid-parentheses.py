class Solution:
    def isValid(self, s: str) -> bool:
        # using Stack
        stack = []
        hmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        for i in s:
            if i in hmap:
                if stack and stack[-1] == hmap[i]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)
        return not stack  #returns true if stack is empty 
    
        
        
        # Solution without stack
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")

            else:        
                return not s