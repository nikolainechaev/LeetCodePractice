class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        hash = set(nums)
        longest = 0
        
        for number in hash:
            if (number - 1) not in hash:
                length = 1
                while (number + length) in hash:
                    length += 1
                longest = max(length, longest)
        return longest
                