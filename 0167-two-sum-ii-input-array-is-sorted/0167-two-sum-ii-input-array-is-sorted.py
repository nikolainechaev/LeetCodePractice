class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        results = {}
        
        for index, number in enumerate(numbers):
            diff = target - number
            if diff in results:
                return [results[diff], index + 1]
            
            results[number] = index + 1