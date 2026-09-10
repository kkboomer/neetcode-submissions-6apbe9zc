class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0]*len(temperatures)
        if len(temperatures) == 1:
            return ans
        for i in range(len(temperatures)):
                # the item we are about to add is greater than the top of the stack
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                add = stack.pop()
                ans[add]= i - add
            stack.append(i)
        return ans 