class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # NEET CODE solution:
        potions.sort()
        res = []
        for s in spells:
            
            L = 0
            R = len(potions) -1
            idx = len(potions)
            while L <=R:
                    m = (L+R)//2
                    
                    if s * potions[m] >= success:
                        R = m - 1
                        idx = m
                    else:
                        L = m +1
                
            res.append(len(potions) - idx)
        return res
        
        
        
        #leet code solution:
#         sortedSpells = [(spell, index) for index, spell in enumerate(spells)]
    
#         sortedSpells.sort()
#         potions.sort()
        
#         answer = [0] * len(spells)
#         m = len(potions)
#         potionIndex = m - 1
        
#         for spell, index in sortedSpells:
#             while potionIndex >= 0 and (spell * potions[potionIndex]) >= success:
#                 potionIndex -= 1
#             answer[index] = m - (potionIndex + 1)
        
#         return answer