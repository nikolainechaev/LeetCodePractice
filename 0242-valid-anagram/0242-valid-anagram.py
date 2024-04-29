class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        sDict, tDict = {}, {}
        
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)

        for c in sDict:
            if sDict[c] != tDict.get(c, 0):
                return False
        return True