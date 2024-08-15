class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        finalIndexes = []
        dict = {}

        for ind, num in enumerate(nums):
            if num in dict:
                finalIndexes.append(num)
            dict[num] = ind
        return finalIndexes        