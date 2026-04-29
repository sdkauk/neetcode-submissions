class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS = {}
        countT = {}

        for i, char in enumerate(s):
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1
        for i, char in enumerate(t):
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        return countS == countT

        