class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L <= R:
            if not self.isAlphaNum(s[L]):
                L += 1
            elif not self.isAlphaNum(s[R]):
                R -= 1
            elif s[L].lower() != s[R].lower():
                return False
            else:
                L += 1
                R -= 1
        
        return True
    
    def isAlphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


