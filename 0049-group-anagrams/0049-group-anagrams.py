class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for string in strs:
            alphabet = [0] * 26
            for char in string:
                alphabet[ord('a') - ord(char)] += 1
            storage[tuple(alphabet)].append(string)
        return list(storage.values())