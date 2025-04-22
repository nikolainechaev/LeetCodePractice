class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list) 
        for string in strs:
            alphabet = [0] * 26 # [0, 0, 0, ....]
            for char in string:
                alphabet[ord(char) - ord('a')] += 1
            bucket[tuple(alphabet)].append(string)
        return list(bucket.values())
