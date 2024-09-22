class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for index, number in enumerate(nums2):
            nums1[m + index] = number
            print(n+index)
        nums1.sort()
        return nums1