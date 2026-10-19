class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #other optimized, hash, and check after the thing is done for count ==1
        # xor 
        xor_sum = 0
        for x in nums:
            xor_sum ^= x
        return xor_sum