class Solution:
    def twoSum(self, nums:[int], target:int) -> List[int]: 
        store = {}
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff in store:
                return [store[diff], index]
            store[number] = index
        return