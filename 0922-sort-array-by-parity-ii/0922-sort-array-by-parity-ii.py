class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        E = 0
        O = 1
        
        while E < len(nums) and O < len(nums):
            if nums[E] % 2 == 0:
                E+=2
            elif nums[O] %2:
                O+=2
            else:
                nums[O], nums[E] = nums[E], nums[O]
                
                E+=2
                O+=2
        return nums