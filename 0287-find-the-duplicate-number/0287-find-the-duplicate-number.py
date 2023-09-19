class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     s.add(i)

        S = 0
        F = 0
        while True:
            S = nums[S]
            F = nums[nums[F]]
            if S == F:
                break 
            
        X = 0
        while True:
            X = nums[X]
            S = nums[S]

            if X == S:
                return S
