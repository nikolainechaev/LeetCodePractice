class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list) # creates dict
        
        for str in strs:
            alphabet = [0] * 28 # creates a-z placeholders
            for char in str:
                alphabet[ord(char) - ord('a')] += 1 # insert 1s in alphabet order for each char into alphabetList
                
            dict[tuple(alphabet)].append(str) # take finalList and create keys out of list from alphabetList and assign related string
        return dict.values()
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
#                       , strs: List[str]) -> List[List[str]]:
        
#         finalList = defaultdict(list)  # creates list dict
        
#         for string in strs:
#             alphabetList = [0] * 26    # creates a-z placeholders
            
#             for letter in string:
#                 alphabetList[ord(letter) - ord('a')] += 1 # insert 1s in alphabet order for each char into alphabetList
        
#             finalList[tuple(alphabetList)].append(string) 
# # take finalList and create keys out of list from alphabetList and assign related string
        
#         return finalList.values() # return only values within one list


