class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        storage = defaultdict(list)

        for string in strs:
            alphaKey = [0] * 26
            for char in string:
                alphaKey[ord(char) - ord("a")] += 1
            storage[tuple(alphaKey)].append(string)
        return list(storage.values())