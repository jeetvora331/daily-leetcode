class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using array indices 
        
        count = {}
        freq = [[] for _ in range(len(nums) +1)]
        
        for n in nums:
            count[n] = 1+ count.get(n,0)
        
        for key , val in count.items():
            freq[val].append(key)
        
        res = []
        for i in reversed(range(len(freq))):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        # #pythonic Solution
        # arr =  collections.Counter(nums).most_common(k)
        # res = []
        # for num , cnt in arr:
        #     res.append(num)
        # return res