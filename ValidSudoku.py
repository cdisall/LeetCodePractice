class Solution:
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            if not self.valid(row):
                return False
        # Check columns
        for col in zip(*board):
            if not self.valid(col):
                return False
        # Check squares
        l = range(0, 7, 3)
        for i in l:
            for j in l:
                # Create a 9 element list for each 3x3 square in the board
                sq = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.valid(sq):
                    return False
        return True

    def valid(self, l):
        l = [i for i in l if i != "."]
        # Check that elements are all unique in the set l
        if len(set(l)) == len(l):
            return True
        return False