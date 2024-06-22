class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
    
    
        for string in strs:
            position = [0] * 26
            for letter in string:
                position[ord(letter) - ord('a')] += 1
            dict[tuple(position)].append(string)
        return dict.values()

        
        
                
                
         