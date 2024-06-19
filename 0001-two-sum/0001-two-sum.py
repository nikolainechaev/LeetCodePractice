class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        dict = {}
        
        for ind, num in enumerate(nums):
            diff = target - num 
            if diff in dict:
                return [dict[diff], ind]
            dict[num] = ind
        return
            
        