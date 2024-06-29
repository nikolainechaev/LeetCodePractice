class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict, list, result = {}, [[] for i in range(len(nums) +1)], []
        
        for number in nums: 
            dict[number] = 1 + dict.get(number, 0)
        for number, quantity in dict.items():
            list[quantity].append(number)
        for i in range(len(list) -1, 0, -1):
            for j in list[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




#         dict = {}
#         list = [[] for i in range(len(nums) + 1)]
        
#         for number in nums:
#             dict[number] = 1 + dict.get(number, 0)
#         for number, q in dict.items():
#             list[q].append(number)
        
#         results = []
        
#         for i in range(len(list) -1, 0, -1):
#             for j in list[i]:
#                 results.append(j)
#                 if len(results) == k:
#                     return results
            






#         dict = {}
#         list = [[] for i in range(len(nums) + 1)]
#         results = []
    
#         for number in nums: 
#             dict[number] = 1 + dict.get(number, 0)
    
#         for number, quantity in dict.items():
#             list[quantity].append(number)

#         for i in range(len(list) -1, 0, -1): 
#             # Mistake: iterrated through "nums", but need to iterate through "list"
#             #Also forgot to create another iteration for number in list[i]:
#             for number in list[i]:
#                 results.append(number)
#                 if len(results) == k: # Used "2" instead of "k"
#                     return results
        
        
        
        
#         dict, list = {}, [[] for i in range(len(nums) + 1)]
#         for number in nums:
#             dict[number] = 1 + dict.get(number, 0)
#         for number, quantity in dict.items():
#             list[quantity].append(number)
#         result = []
#         for i in range(len(list) -1, 0, -1):
#             for number in list[i]:
#                 result.append(number)
#                 if len(result) == k:
#                     return result
                