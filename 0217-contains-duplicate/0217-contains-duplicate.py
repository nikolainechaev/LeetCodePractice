class Solution: 
    def containsDuplicate(self, nums:[int]) -> bool:
        bucket = set()
        for digit in nums:
            if digit in bucket:
                return True
            bucket.add(digit)
        return False