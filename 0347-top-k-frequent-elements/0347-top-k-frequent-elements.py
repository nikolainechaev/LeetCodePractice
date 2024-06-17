class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        
        dict = {}
        list = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        for num, quant in dict.items():
            list[quant].append(num)
        
        
        finalResult = []
        for num in range(len(list)-1, 0, -1):
            for value in list[num]:
                finalResult.append(value)
                if len(finalResult) == k:
                    return finalResult