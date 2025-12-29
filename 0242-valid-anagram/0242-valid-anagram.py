class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        storageS, storageT = {}, {}

        for i in range(len(s)):
            storageS[s[i]] = 1 + storageS.get(s[i], 0)
            storageT[t[i]] = 1 + storageT.get(t[i], 0)
        return storageS == storageT