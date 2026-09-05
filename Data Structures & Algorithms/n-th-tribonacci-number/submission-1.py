class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0, 1, 1
        if n == 0:
            return a
        elif 0 < n <= 2:
            return b
        else:
            for m in range(2, n):
                a, b, c = b, c, a + b + c
            return c