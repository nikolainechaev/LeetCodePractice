class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for int in nums:
            if int in hashset:
                return True
            hashset.add(int)
        return False
