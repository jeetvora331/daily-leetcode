class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        mx = max(candies)
        # res = []
        # for i in range(len(candies)):
        #     res.append(candies[i] + e >= mx)
        # return res
        
        return [candies[i] +e >= mx for i in range(len(candies))]