class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        source = defaultdict(list)
        
        for string in strs:
            order = [0] * 26
            for character in string: 
                order[ord(character) - ord('a')] += 1
            source[tuple(order)].append(string)
        return source.values()