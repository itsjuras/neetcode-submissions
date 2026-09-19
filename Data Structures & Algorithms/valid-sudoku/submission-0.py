class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False

        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False

        boxes = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    key = (r // 3, c // 3)
                    if key not in boxes:
                        boxes[key] = set()
                        boxes[key].add(board[r][c])
                    else:
                        if board[r][c] in boxes[key]:
                            return False
                        boxes[key].add(board[r][c])
        return True



