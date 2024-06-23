class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        
        dict = {}
        list = [[] for i in range(len(nums) + 1)] #forgot about "+1"
        
        for number in nums:
            dict[number] = 1 + dict.get(number, 0) #forgot about "dict.get(number, 0)" also used "+=" instead of "="
        for number, quantity in dict.items():  #forgot about ".items()", also forgot about what goes first quantity or number...
            list[quantity].append(number)
        
        results = []
        
        for i in range(len(list) -1, 0, -1):  #forgot about "len()"
            for j in list[i]:
                results.append(j)
                if len(results) == k:
                    return results
            
            
        
        