class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(n):
            if n == 0:
                return 0
            elif n < 0:
                return float('inf')
            elif n in cache:
                return cache[n]
            count = float('inf') # we set it so big so the next coin combo will fit
            for i in range(len(coins)):
                count = min(count , 1+dfs(n - coins[i]))
            cache[n] = count
            return count
        res = dfs(amount)
        return -1 if res == float('inf') else res