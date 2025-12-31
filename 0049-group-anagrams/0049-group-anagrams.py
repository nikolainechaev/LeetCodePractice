class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            order = [0] * 26
            for char in string:
                order[ord(char) - ord("a")] += 1
            result[tuple(order)].append(string)
        return list(result.values())
