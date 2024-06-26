class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1] # where is sum of prefixes here?
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i] #forgot that we need to update postfix variable with number from "nums"
        return result
        
        
        
        
        
        
        
        
#         res = [1] * len(nums)
        
#         for i in range(1, len(nums)):
#             res[i] = res[i - 1] * nums[i - 1]
#         postfix = 1
#         for i in range(len(nums) -1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res
            