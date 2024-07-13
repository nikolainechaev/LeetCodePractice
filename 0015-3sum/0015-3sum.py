class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        results = []
        
        for index, number in enumerate(nums):
            if number > 0:
                break
            if index > 0 and number == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1 #why l = index + 1, why we can't use just "l = 1"
            while l < r: 
                threeSum = number + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    results.append([number, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:      # forgot to add 'while l < r'
                        l += 1
        return results
                