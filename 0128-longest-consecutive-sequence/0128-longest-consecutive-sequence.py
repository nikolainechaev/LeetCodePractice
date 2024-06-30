class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        
        for number in hashSet:
            if (number - 1) not in hashSet:
                length = 1
                while (number + length) in hashSet:
                    length += 1
                longest = max(length, longest)
        return longest
                