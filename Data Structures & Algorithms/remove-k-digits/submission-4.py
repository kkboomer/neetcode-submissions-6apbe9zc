class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 1:
            return "0"
        stack = []
        for x in num:
            while stack and k > 0 and stack[-1]> x:
                stack.pop()
                k -= 1
            stack.append(x)
        # k may still exist after we finish case of strictly increasing
        while k > 0 and stack:
            stack.pop()
            k -=1
        res = "".join(stack).lstrip("0")
        return res if res else "0"
