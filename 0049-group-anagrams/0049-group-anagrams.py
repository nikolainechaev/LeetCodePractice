class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for string in strs:
            order = [0] * 26
            for char in string:
                place = ord(char) - ord("a")
                order[place] += 1
            anagram_groups[tuple(order)].append(string)
        return list(anagram_groups.values())
