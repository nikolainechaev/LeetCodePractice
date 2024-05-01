class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {}
        for l in range(len(s)):
            dictS[s[l]] = 1 + dictS.get(s[l], 0)
            dictT[t[l]] = 1 + dictT.get(t[l], 0)
        for c in dictS:
            if dictS[c] != dictT.get(c, 0):
                return False
        return True