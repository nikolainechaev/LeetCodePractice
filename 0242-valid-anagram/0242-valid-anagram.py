class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        firstDict = dict()
        secondDict = dict()

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            firstDict[t[c]] = firstDict.get(t[c], 0) + 1
            secondDict[s[c]] = secondDict.get(s[c], 0) + 1
        
        for item in firstDict:
            if firstDict[item] != secondDict.get(item, 0):
                return False

        return True
