class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNumber = str(x)
        
        l, r = 0, len(strNumber) - 1
        
        while l < r: 
            if strNumber[l] != strNumber[r]:
                return False
            l, r = l + 1, r - 1
        return True