class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        someList = list(s)
        for char in range(0, len(someList) - 1, 2*k):
            someList[char:char + k] = reversed(someList[char:char + k])
        return "".join(someList)