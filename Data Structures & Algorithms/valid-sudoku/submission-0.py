class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if ((board[i][j] in row_check[i]) or (board[i][j] in col_check[j]) or
                    (board[i][j] in box_check[(i//3,j//3)])):
                    return False
                row_check[i].add(board[i][j])
                col_check[j].add(board[i][j])
                box_check[(i // 3, j // 3)].add(board[i][j])
        return True

        