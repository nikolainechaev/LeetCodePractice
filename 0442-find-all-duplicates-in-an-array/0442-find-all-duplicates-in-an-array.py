class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []
        d = {}
        
        for index, number in enumerate(nums):
            if number in d:
                results.append(number)
            d[number] = index
        return results
           
            
            