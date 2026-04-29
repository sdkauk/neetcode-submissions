class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        arr = []
        for count, item in counts.items():
            arr.append([item, count])
        
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output
