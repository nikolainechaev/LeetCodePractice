class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        bucketS = {}
        bucketT = {}
        
        for char in range(len(t)):
            bucketS[s[char]] = 1 + bucketS.get(s[char], 0)
            bucketT[t[char]] = 1 + bucketT.get(t[char], 0)

        for char in bucketS:
            if bucketS[char] != bucketT.get(char, 0):
                return False
        return True
        