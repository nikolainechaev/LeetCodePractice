class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.alphanum(s[left]): #forgot about 's[left]'
                left += 1
            while right > left and not self.alphanum(s[right]): #forgot about 's[right]'
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1                  #forgot about whole this line
        return True
        
    def alphanum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l, r = 0, len(s) - 1
        
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while r > l and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1
#         return True
    
#     def alphanum(self, c: str) -> bool:
#         return (ord('A') <= ord(c) <= ord('Z') or
#                ord('a') <= ord(c) <= ord('z') or
#                ord('0') <= ord(c) <= ord('9'))

