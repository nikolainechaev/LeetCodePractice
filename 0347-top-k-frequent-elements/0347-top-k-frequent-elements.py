class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict, list = {}, [[] for i in range(len(nums) + 1)]
        for number in nums:
            dict[number] = 1 + dict.get(number, 0)
        for number, quantity in dict.items():
            list[quantity].append(number)
        result = []
        for i in range(len(list) -1, 0, -1):
            for number in list[i]:
                result.append(number)
                if len(result) == k:
                    return result
                