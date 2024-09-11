class Solution:
    def validateLine(self, line: List[str]):
        return len(line) == len(set(line))

    def get_squares(self, board):
        squares = []
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                square = []
                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        if board[row][col]!='.':
                            square.append(board[row][col])
                squares.append(square)
        return squares

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validate line
        for line in board:
            line = list(filter(lambda x: x != '.', line))
            if not self.validateLine(line):
                print('line', line)
                return False
        #validate col
        for i in range(9):
            col = []
            for j in range(9):
                if (board[j][i] != '.'):
                    col.append(board[j][i])

            if not self.validateLine(col):
                return False
        #get a square
        squares = self.get_squares(board)
        for sq in squares:
            if not self.validateLine(sq):
                print('sq', sq)
                return False         

        return True