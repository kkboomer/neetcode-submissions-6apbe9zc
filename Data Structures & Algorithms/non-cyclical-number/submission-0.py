class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            h = 0
            while n:
                h += (n % 10) ** 2
                n //= 10
            if h == 1:
                return True
            elif h in s:
                return False
            n = h
            s.add(h)