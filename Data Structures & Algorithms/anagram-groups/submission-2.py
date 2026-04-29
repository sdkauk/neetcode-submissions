class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ac = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[(ord('a') - ord(char))] += 1
        
            tc = tuple(count)
            if tc in ac:
                ac[tc].append(s)
            else:
                ac[tc] = [s]
        
        return list(ac.values())
