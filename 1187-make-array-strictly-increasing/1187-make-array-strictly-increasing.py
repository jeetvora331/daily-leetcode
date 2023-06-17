class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        n = len(arr2)
        
        for i in range (len(arr1)):
            dp2 = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if arr1[i] > prev:
                    dp2[arr1[i]] = min (dp2[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2,prev)
                if idx < n:
                    dp2[arr2[idx]] = min(dp2[arr2[idx]], dp[prev]+1)
            dp = dp2
        
        return min(dp.values()) if dp else -1