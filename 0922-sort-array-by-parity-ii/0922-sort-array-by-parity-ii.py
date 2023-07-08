class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        E = 0
        O = 1
        
        while E < len(nums) and O < len(nums):
            if nums[E] % 2 == 0:
                E += 2
            elif nums[O] % 2 == 0:
                nums[O], nums[E] = nums[E], nums[O]  # Use assignment operator (=) instead of comparison operator (==)
                E += 2
                O += 2
            else:
                O += 2  # Increment O if neither E nor O is even
        
        return nums
