class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        
        def helper(l ,r):
            if (l,r ) in cache:
                return cache[(l,r)]
            
            if l>r:
                return 0
            if l==r:
                return 1
            
            if s[l] == s[r]:
                cache[(l,r)]=  helper(l+1, r-1) +2
            else:
                cache[(l,r)] = max(helper(l, r-1) , helper(l+1,r))
            
            return cache[(l,r)]
        
        res = helper(0 , len(s) -1)
        return res    
        