class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        
        for i, c in enumerate(s):
            lastIdx[c] = i
            
        res = []
        size = 0
        end = 0
        
        for i , c in enumerate(s):
            size +=1
            end = max(end , lastIdx[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res
        
#         count = {}
#         res = []
#         i, length = 0, len(S)
#         for j in range(length):
#             c = S[j]
#             count[c] = j

#         curLen = 0
#         goal = 0
#         while i < length:
#             c = S[i]
#             goal = max(goal, count[c])
#             curLen += 1

#             if goal == i:
#                 res.append(curLen)
#                 curLen = 0
#             i += 1
#         return res
