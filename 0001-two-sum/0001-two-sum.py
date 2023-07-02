class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:

        # hash = defaultdict(int)
        # res = []
        # for i in range(len(nums)):
        #     A = t - nums[i]
        #     if A in hash:
        #         return [hash[A], i]
        #     hash[nums[i]] = i

        hash = {}
        for i , n in enumerate(nums):
            diff = t - n
            if diff in hash:
                return [i , hash[diff]]
            hash[n] = i

            