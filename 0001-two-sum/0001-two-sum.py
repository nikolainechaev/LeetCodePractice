class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        dict = {}
        
        for index, number in enumerate(nums):
            difference = target - number
            if difference in dict:
                return [dict[difference], index]
            dict[number] = index