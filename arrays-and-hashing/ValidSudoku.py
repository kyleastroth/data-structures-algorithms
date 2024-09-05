class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # 1. Hash set for each row
        # 2. Hash set for each column
        # 3. Hash set for each 3x3 grid
        # Create indices for 3x3 board (do this using integer division & floor (rounding down))

        # cols = {} # (key, val) pair is (col, set of nums in row), ex for row 1: key = 0, val = {5, 3, 7}
        cols = {k: [] for k in range(9)}
        
        # rows = {} # (key, val) pair is (row, set of nums in col)
        rows = {k: [] for k in range(9)}
        
        # three_squares = {} # (key, val) pair is ((r/3, c/3), set of nums in square), ex for square (1,1): key = (0,0), val = {5, 3, 6, 9, 8}
        three_squares = {}
        for k1 in range(3):
            for k2 in range(3):
                three_squares[(k1, k2)] = []


        for r in range(9):
            for c in range(9):
                # If empty space (represented by ".") then skip
                if board[r][c] == ".": 
                    continue
                    
                # Check if found duplicate
                sqr1 = r // 3
                sqr2 = c // 3

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in three_squares[(sqr1, sqr2)]):
                    return False

                # Add to hash tables:
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                three_squares[(sqr1, sqr2)].append(board[r][c])
        
        return True

        # Time complexity: iterate over entire matrix
        # Space Complexity: 3 hash sets
