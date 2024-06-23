class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        
        dict = {}
        list = [[] for i in range(len(nums) + 1)] #forgot about "+1"
        
        for number in nums:
            dict[number] = 1 + dict.get(number, 0) #forgot about "dict.get(number, 0)" also used "+=" instead of "="
        for quantity, number in dict.items():  #forgot about ".items()"
            list[number].append(quantity)
        
        results = []
        
        for i in range(len(list) -1, 0, -1):  #forgot about "len()"
            for j in list[i]:
                results.append(j)
                if len(results) == k:
                    return results
            
            
        
        