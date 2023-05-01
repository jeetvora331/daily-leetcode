class Solution:
    def average(self, salary: List[int]) -> float:
        res = sum(salary) - max(salary) -min(salary)
        return res/(len(salary) - 2)
        