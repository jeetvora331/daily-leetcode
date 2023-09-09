class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Create an array to store the number of combinations that add up to each index up to the target
        # Initialize the first element to 1, since there is 1 way to add up to 0
        dp = [0] * (target + 1)
        dp[0] = 1
        
        # Sort the input array to make sure we consider combinations in the correct order
        nums.sort()
        
        # Iterate through each index up to the target
        for i in range(1, target + 1):
            # Iterate through each number in the input array
            for num in nums:
                # If the number is greater than the current index, break out of the inner loop
                if num > i:
                    break
                # Otherwise, add the number of combinations that add up to the current index minus the current number
                # to the current number of combinations that add up to the current index
                dp[i] += dp[i - num]
        
        # Return the number of combinations that add up to the target
        return dp[target]