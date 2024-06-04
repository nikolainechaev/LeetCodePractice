class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for string in strs:
            order = [0] * 28
            for character in string: 
                order[ord(character) - ord('a')] += 1
            results[tuple(order)].append(string)
        return results.values()
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
#                       , strs: List[str]) -> List[List[str]]:
        
#         finalList = defaultdict(list)  # creates list dict
        
#         for string in strs:
#             alphabetList = [0] * 26    # creates a-z placeholders
            
#             for letter in string:
#                 alphabetList[ord(letter) - ord('a')] += 1 # insert 1s in alphabet order for each char into alphabetList
        
#             finalList[tuple(alphabetList)].append(string) 
# # take finalList and create keys out of list from alphabetList and assign related string
        
#         return finalList.values() # return only values within one list


