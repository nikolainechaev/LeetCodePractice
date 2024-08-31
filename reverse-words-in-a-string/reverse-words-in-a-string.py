class Solution:
    def reverseWords(self, s: str) -> str:
        
        arrOfWords = s.split()
        reversedWordsArr = arrOfWords[::-1]
        finalString = ' '.join(reversedWordsArr)
        
        return finalString