class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) - 1
        L = 0
        R = n
        while L < R:
            while L < R and not self.isAlphaNum(s[L]):
                L += 1
            while R > L and not self.isAlphaNum(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            else:
                L+=1
                R-=1
        
        return True

    def isAlphaNum(self, val):
        return (ord('A') <= ord(val) <= ord('Z') or
                ord('a') <= ord(val) <= ord('z') or
                ord('0') <= ord(val) <= ord('9'))

