class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        storage = set(nums)
        
        for number in storage:
            if (number-1) not in storage:
                length = 1
                while (number + length) in storage:
                    length += 1
                longest = max(length, longest)
        return longest