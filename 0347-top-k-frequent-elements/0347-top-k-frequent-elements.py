class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, res, list = {}, [], [[] for i in range(len(nums) + 1)] #forgot "+1"
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for number, count in count.items():
            list[count].append(number)
        for number in range(len(list) -1, 0, -1):
            for j in list[number]:  #forgot about whole this iteration line
                res.append(j)
                if len(res) == k:
                    return res
            
            