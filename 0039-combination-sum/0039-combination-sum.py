class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        answer = []
        def helper(can , currIndex , currSum, currComb, target):
            if currSum > target:
                return
            if currSum == target:
                answer.append(currComb)
            
            for i in range(currIndex , len(can)):
                helper(can, i , currSum + can[i], currComb + [can[i]] , target)
            
        helper(can , 0,0, [], target)
        return answer
                
        