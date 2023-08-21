class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        curr = s + s
        return s in curr[1:-1]