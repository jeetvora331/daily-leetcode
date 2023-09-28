class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_numbers = []
        odd_numbers = []
        
        # Separate even and odd numbers
        for num in nums:
            if num % 2 == 0:
                even_numbers.append(num)  # Even number found
            else:
                odd_numbers.append(num)   # Odd number found
        
        # Combine even and odd numbers, placing even numbers first
        result = even_numbers + odd_numbers
        
        return result  # Return the sorted array