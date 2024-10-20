from typing import List

def isRowValid(row: List[str]) -> bool:
    digits = set()

    for square in row:
        if square == '.':
            continue

        if square in digits:
            return False
        
        digits.add(square)

    return True

def areRowsValid(board: List[List[str]]) -> bool:
    return all(map(isRowValid, board))

def areColumnsValid(board: List[List[str]]) -> bool:
    for col in range(9):
        digits = set()

        for row in range(9):
            square = board[row][col]
            if square == '.':
                continue

            if square in digits:
                return False

            digits.add(square)

    return True

def boxOffsets():
    for i in range(3):
        for j in range(3):
            yield (i * 3, j * 3)
    

def areBoxesValid(board: List[List[str]]) -> bool:
    offsets = boxOffsets()

    for _ in range(9):
        digits = set()
        offset = next(offsets)
        iOffset = offset[0]
        jOffset = offset[1]

        for i in range(3):
            for j in range(3):
                square = board[i + iOffset][j + jOffset]
                if square == '.':
                    continue

                if square in digits:
                    return False
                
                digits.add(square)
    
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return areRowsValid(board) and areColumnsValid(board) and areBoxesValid(board)


solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))