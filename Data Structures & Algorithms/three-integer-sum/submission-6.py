class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            if nums[i] == nums[i-1] and i > 0: continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = -(nums[j] + nums[k])
                if s == nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif s > nums[i]:
                    j += 1
                else:
                    k -= 1
        return res
