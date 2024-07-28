class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mi = (l + r) // 2
            if nums[mi] > target:
                r = mi -1
            elif nums[mi] < target:
                l = mi + 1
            else:
                return mi
        return -1
            