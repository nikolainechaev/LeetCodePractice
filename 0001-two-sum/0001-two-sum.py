class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, number in enumerate(nums):
            catch = target - number
            if catch in map:
                return [map[catch], index]
            map[number] = index