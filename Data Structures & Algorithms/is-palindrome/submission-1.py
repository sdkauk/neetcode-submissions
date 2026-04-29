class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = [c.lower() for c in s if c.isalnum()]
        
        n = len(cleaned)
        frontwards = [0] * n
        backwards = [0] * n

        for i, char in enumerate(cleaned):
            frontwards[i] = char.lower()
            backwards[(n - i) - 1] = char.lower()
        
        return backwards == frontwards

            
