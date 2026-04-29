# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs, 0, len(pairs) - 1)
        return pairs
    def sort(self, arr, s, e):
        #bound case
        if e - s + 1 <= 1:
            return

        #assign your pivot
        pivot = arr[e]

        #create a pointer to the first element
        left = s

        #partion: put elements smaller than the pivot on the left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
            
        arr[e] = arr[left]
        arr[left] = pivot

        self.sort(arr, s, left - 1)
        self.sort(arr, left + 1, e)

