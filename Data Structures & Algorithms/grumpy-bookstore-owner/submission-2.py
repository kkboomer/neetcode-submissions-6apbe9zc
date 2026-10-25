class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
       m = minutes
       n = len(customers)
       res = sum(customers[i] for i in range(n) if grumpy[i] == 0)
       bonus = sum(customers[i] for i in range(m) if grumpy[i] == 1)
       current_bonus = bonus
       for r in range(m,n):
        l = r - m
        current_bonus += customers[r] * grumpy[r] - customers[l] * grumpy[l]
        bonus = max(bonus, current_bonus)
       return res + bonus 