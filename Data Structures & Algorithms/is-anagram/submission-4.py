class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT = {}
        countS = {}

        for char in s:
            if char in countS:
                countS[char] = countS[char] + 1
            else:
                countS[char] = 1

        for char in t:
            if char in countT:
                countT[char] = countT[char] + 1
            else:
                countT[char] = 1
            
        return countS == countT
