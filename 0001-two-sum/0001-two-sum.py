class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [dict[diff], index]
            dict[num] = index
        return
            
            
            


























# class Solution: 
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
        
#         for i, d in enumerate(nums):
#             diff = target - d
#             if diff in dict:
#                 return [dict[diff], i]
#             dict[d] = i
#         return 
            
                