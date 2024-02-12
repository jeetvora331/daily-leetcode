class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        visited = defaultdict(int)
        for n in nums:
            visited[n] += 1

            if visited[n]>len(nums)//2:
                return n