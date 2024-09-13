class Solution:
    def reverseWords(self, s: str) -> str:
        
        source = s.split()
        reverseSource = source[::-1]
        result = ' '.join(reverseSource)
        
        return result