class Solution:
    def isPalindrome(self, s: str) -> bool:

        allchars = list(s)
        chars = []
        for char in allchars:
            if char.isalnum():
                chars.append(char.lower())

        l = 0
        r = len(chars) - 1
        while l < r:
            if chars and chars[l] != chars[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
            