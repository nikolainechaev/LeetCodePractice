class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.insert(1, target)
        nums.sort()
        
        for index, number in enumerate(nums):
            if number == target:
                return index