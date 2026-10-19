class Solution:
    def hammingWeight(self, n: int) -> int:
        power = 1
        total = 0
        for i in range(32):
            check = power << i
            if check & n != 0: 
                total += 1
        return total