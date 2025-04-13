class Solution: 
    def containsDuplicate(self, nums:[int]) -> bool:
        storage = set()
        for number in nums:
            if number in storage:
                return True
            storage.add(number)
        return False
