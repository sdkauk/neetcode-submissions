class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ac = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1

            tc = tuple(counts)
            if tc in ac:
                ac[tc].append(s)
            else:
                ac[tc] = [s]

        return list(ac.values())

