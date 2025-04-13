class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        dict = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in dict:
                return [dict[diff], index]
            dict[number] = index
            