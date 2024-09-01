class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        for character in s:
            if character in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[character]:
                    return False
            else:
                stack.append(character)
        return not stack