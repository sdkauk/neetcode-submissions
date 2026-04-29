class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) 
        L, R = 0, len(matrix) * n - 1

        while L <= R:
            m = (L + R) // 2
            row = m // n
            pos = m % n
            if target > matrix[row][pos]:
                L = m + 1
            elif target < matrix[row][pos]:
                R = m - 1

            else:
                return True

        return False