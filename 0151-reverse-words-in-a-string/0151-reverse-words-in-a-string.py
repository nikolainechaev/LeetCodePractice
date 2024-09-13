class Solution:
    def reverseWords(self, s: str) -> str:
        
        arrayOfWords = s.split()
        reverseArr = arrayOfWords[::-1]
        finalString = ' '.join(reverseArr)
        
        return finalString