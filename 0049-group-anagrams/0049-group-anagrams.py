class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list) 
        
        for string in strs:
            alphabet = [0] * 28
            for char in string:
                alphabet[ord(char) - ord('a')] += 1
            dict[tuple(alphabet)].append(string)
        return dict.values()
        
                
                
         