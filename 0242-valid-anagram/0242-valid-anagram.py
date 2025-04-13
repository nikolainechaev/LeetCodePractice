class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        tBucket = dict()
        sBucket = dict()

        if len(s) != len(t):
            return False

        for letter in range(len(s)):
            tBucket[t[letter]] = tBucket.get(t[letter], 0) + 1
            sBucket[s[letter]] = sBucket.get(s[letter], 0) + 1
        
        for letter in sBucket:
            if sBucket[letter] != tBucket.get(letter, 0):
                return False

        return True