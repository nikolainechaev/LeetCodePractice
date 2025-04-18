class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        bucket = dict()
        for index, number in enumerate(nums):
            diff = target - number
            if diff in bucket:
                return[bucket[diff], index]
            bucket[number] = index
