class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniqueSortedArr = set(nums)
        
        for number in uniqueSortedArr:
            if (number - 1) not in uniqueSortedArr:
                length = 1
                while (number + length) in uniqueSortedArr:
                    length += 1
                longest = max(length, longest)
        return longest