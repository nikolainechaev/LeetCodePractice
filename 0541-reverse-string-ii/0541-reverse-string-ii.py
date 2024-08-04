class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        someList = list(s)
        for i in range(0, len(someList), 2 * k):
            someList[i:i + k] = reversed(someList[i:i + k])
        return "".join(someList)