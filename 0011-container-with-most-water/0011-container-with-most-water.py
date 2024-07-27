class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        
        l, r = 0, len(height) - 1
        
        while l < r: 
            result = max(result, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return result