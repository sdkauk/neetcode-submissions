class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue
                
                square = (row // 3, col // 3)

                if (num in rows[row] or num in cols[col] or num in squares[square]):
                    return False

                cols[col].add(num)
                rows[row].add(num)
                squares[square].add(num)
                
        return True