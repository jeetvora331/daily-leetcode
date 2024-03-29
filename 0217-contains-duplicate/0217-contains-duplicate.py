class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return not (len(set(nums))==len(nums))
    
#         visited = {}
#         for i in nums:
#             if i in visited:
#                 return True
#             else :
#                 visited[i]=True
        # return False
    
        visited = set()
        for i in nums:
            if i in visited:
                return True
            else:
                visited.add(i)
        
        return False