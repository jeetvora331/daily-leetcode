class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#         if op < n : add open 
#         if  cl < op : add close 
        # if op == cl == n return True

        
        res = []
        stack = []
        op = 0
        cl = 0
        
        def helper(op, cl):
            if op == cl == n :
                a = "".join(stack)
                res.append(a)
                
            if op < n :
                stack.append("(")
                helper(op+1 , cl)
                stack.pop()
            
            if cl<op:
                stack.append(")")
                helper(op , cl + 1)
                stack.pop()
            
        helper(op,cl)
        return res 
                
                