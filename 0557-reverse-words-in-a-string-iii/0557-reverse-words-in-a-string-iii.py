class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        res = []
        for word in s.split(" "):
            a = word[::-1]
            res.append(a)
        return " ".join(res)
        