class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))
        
        pair.sort()
        
        for p , s in reversed(pair):
            t = (target-p)/s
            stack.append([t])
            
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
                
        return len(stack)