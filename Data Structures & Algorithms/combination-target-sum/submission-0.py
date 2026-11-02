class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # if that sum is the target, we add to our resturn list.
        res =[]
        def helper(i, curr_target, way):
            if curr_target == 0:
                res.append(way[:])
                return
            if curr_target < 0 or i == len(candidates):
                return
            # here we take or leave it
            way.append(candidates[i])
            helper(i, curr_target -candidates[i], way)
            way.pop() # this is the "backtrack"
            helper(i+1, curr_target, way)
        helper(0, target, [])
        return res