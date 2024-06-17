class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        dictResult = {}
        
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in dictResult:
                return [dictResult[diff], ind]
            dictResult[num] = ind
        return
            
            
        