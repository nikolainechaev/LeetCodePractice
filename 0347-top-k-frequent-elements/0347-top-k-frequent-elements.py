class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sortArray = []
        for num, quant in count.items():
            sortArray.append([quant, num])
        sortArray.sort()

        result = []
        while len(result) < k:
            result.append(sortArray.pop()[1])
        return result