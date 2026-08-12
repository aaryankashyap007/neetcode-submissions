class Solution:
    def check_duplicate(self, lst: List[int]) -> bool:
        arr = [0] * 9
        for num in lst:
            arr[num - 1] += 1
        for num in arr:
            if num > 1:
                return True
        return False

    def check_row(self, row: List[str]) -> bool:
        lst = [int(ch) for ch in row if ch.isdigit()]
        if self.check_duplicate(lst):
            return False
        return True
    
    def check_columns(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr = []
            for j in range(9):
                arr.append(board[j][i])
            if self.check_row(arr) == False:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.check_row(row) == False:
                return False
        
        if self.check_columns(board) == False:
            return False
        
        arr = []
        for i in range(0, 3):
            for j in range(0, 3):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False
            
        arr = []
        for i in range(0, 3):
            for j in range(3, 6):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(0, 3):
            for j in range(6, 9):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(3, 6):
            for j in range(0, 3):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(3, 6):
            for j in range(3, 6):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(3, 6):
            for j in range(6, 9):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(6, 9):
            for j in range(0, 3):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(6, 9):
            for j in range(3, 6):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        arr = []
        for i in range(6, 9):
            for j in range(6, 9):
                arr.append(board[i][j])
        if self.check_row(arr) == False:
            return False

        return True