class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        sortedArray = set(nums)
        
        for number in sortedArray:
            if (number - 1) not in sortedArray:
                length = 1
                while (number + length) in sortedArray:
                    length += 1
                longest = max(length, longest)
        return longest