class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        n = len(s) - 1        
        L = 0
        R = n

        while L < R:
            if not self.alphaNum(s[L]):
                L += 1
            elif not self.alphaNum(s[R]):
                R -= 1
            elif (s[L].lower() != s[R].lower()):
                return False
            else:
                L += 1
                R -= 1
    
        return True

    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


            
