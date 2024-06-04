class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]: 
        dict = {}
        list = [[] for i in range(len(nums) + 1)]
        
        for number in nums: 
            dict[number] = 1 + dict.get(number, 0)
        for number, quantity in dict.items():
            list[quantity].append(number)    # why we can't use just list[quantity] = number ???
        
        response = []
        for i in range(len(list) -1, 0, -1): # need to remember the order of those -1,0,-1 and what they mean
            for number in list[i]:
                response.append(number)
                if len(response) == k:
                    return response
            
            










# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
        
#         for number in nums:
#             count[number] = 1 + count.get(number, 0) # will create a dict that will look like this {1: 3, 2: 1, ... }
#         for number, quantity in count.items():       # will take each pair and create a tuple
#             freq[quantity].append(number)            # will make freq list with reversed variation of count [(3: 1), (1: 2), ...]
            
#         response = []                                # empty list
#         for i in range(len(freq) -1, 0, -1):         # taking freq list and iterate from last item in the list 
#             for number in freq[i]:                   # in freq list we iterate over keys in tuples
#                 response.append(number)              # append each number to response list, until we reach k quantity in response
#                 if len(response) == k:
#                     return response