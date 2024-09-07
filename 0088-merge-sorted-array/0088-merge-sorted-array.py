class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for number in range(n):
            nums1[m + number] = nums2[number]
        nums1.sort()