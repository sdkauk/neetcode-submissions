class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsT = {}
        countsS = {}
        for char in s:
            if char in countsS:
                countsS[char] += 1
            else:
                countsS[char] = 1
            

        for char in t:
            if char in countsT:
                countsT[char] += 1
            else:
                countsT[char] = 1

        return countsS == countsT
        