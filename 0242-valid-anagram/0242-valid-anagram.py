class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDictinary, tDictinary = {}, {}
        if len(s) != len(t):
            return False

        for char in range(len(s)):
            sDictinary[s[char]] = 1 + sDictinary.get(s[char], 0)
            tDictinary[t[char]] = 1 + tDictinary.get(t[char], 0)

        for l in sDictinary:
            if sDictinary[l] != tDictinary.get(l, 0):
                return False
        return True