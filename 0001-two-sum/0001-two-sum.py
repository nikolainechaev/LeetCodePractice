class Solution:
    def twoSum(self, nums: [int], target: int) -> List[int]: 
        
        dict = {}
        
        for ind,  dig in enumerate(nums):
            diff = target - dig
            if diff in dict:
                return [dict[diff], ind]
            dict[dig] = ind
        return
            
            
            
            
        