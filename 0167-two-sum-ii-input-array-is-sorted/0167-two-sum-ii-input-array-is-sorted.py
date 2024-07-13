class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        
        for index, number in enumerate(numbers):
            diff = target - number
            if diff in dict:
                return[dict[diff] + 1, index + 1]
            dict[number] = index
        return