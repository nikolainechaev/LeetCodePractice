class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, d in enumerate(nums):
            diff = target - d
            if diff in dict:
                return [dict[diff], i]
            dict[d] = i
        return
            
            
            
                