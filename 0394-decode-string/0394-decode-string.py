class Solution:
    def decodeString(self, s: str) -> str:
        # Recurssive Solution 
        def helper(i, count, left):
            if i >= len(s):
                return ""
            
            if s[i] =="]":
                left[0] = i
                return ""
            
            if s[i] =="[":
                return int(count)*helper(i+1 , "" , left) + helper(left[0] + 1, "" , left)
            
            if s[i].isnumeric():
                return helper(i+1 , count + s[i], left)
            
            else:
                return s[i] + helper(i+1 , count , left)
            
        left = [0]
        return helper(0 , "" , left)