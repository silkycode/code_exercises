""" This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver. """

class SudokuGrid():
    def __init__(self) -> None:

        self.width = 9
        self.rows = [set() for _ in range(self.width)]
        self.cols = [set() for _ in range(self.width)]
        self.boxes = [set() for _ in range(self.width)]

        self.board = [[0] * 9 for i in range(9)]
        self.valid_state = True

    def insert(self, i: int, j: int, val: int) -> bool:
        if self.board[i][j] != 0:
            return self.update(i, j, val)
        
        row_set, col_set, box_set = self.get_sets(i, j)
        for set in (row_set, col_set, box_set):
            if val in set:
                return False
        else:
            row_set.add(val)
            col_set.add(val)
            box_set.add(val)
            self.board[i][j] = val
            return True
    
    def update(self, i: int, j: int, val: int) -> bool:

        old_val = self.board[i][j]
        self.delete(i, j)

        if not self.insert(i, j, val):
            self.insert(i, j, old_val)
            return False
        return True
    
    def delete(self, i: int, j: int):

        if self.board[i][j] == 0:
            return
        
        val = self.board[i][j]
        row_set, col_set, box_set = self.get_sets(i, j)

        row_set.discard(val)
        col_set.discard(val)
        box_set.discard(val)
        self.board[i][j] = 0

    def get_sets(self, i: int, j: int) -> tuple:
        box_width = int(self.width ** 0.5)
        box_id = (i // box_width) * box_width + (j // box_width)

        return (self.rows[i], self.cols[j], self.boxes[box_id])
    
    def visualize(self) -> None:
        print()
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
                
            row_str = ""
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                row_str += str(val) + " "
            
            print(row_str.strip())
        print()
    
    def easy_preset(self) -> None:
        self.reset_board()
        sudoku.insert(0, 0, 5)
        sudoku.insert(0, 1, 3)
        sudoku.insert(0, 4, 7)

        sudoku.insert(1, 0, 6)
        sudoku.insert(1, 3, 1)
        sudoku.insert(1, 4, 9)
        sudoku.insert(1, 5, 5)

        sudoku.insert(2, 1, 9)
        sudoku.insert(2, 2, 8)
        sudoku.insert(2, 7, 6)

        sudoku.insert(3, 0, 8)
        sudoku.insert(3, 4, 6)
        sudoku.insert(3, 8, 3)

        sudoku.insert(4, 0, 4)
        sudoku.insert(4, 3, 8)
        sudoku.insert(4, 5, 3)
        sudoku.insert(4, 8, 1)

        sudoku.insert(5, 0, 7)
        sudoku.insert(5, 4, 2)
        sudoku.insert(5, 8, 6)

        sudoku.insert(6, 1, 6)
        sudoku.insert(6, 6, 2)
        sudoku.insert(6, 7, 8)

        sudoku.insert(7, 3, 4)
        sudoku.insert(7, 4, 1)
        sudoku.insert(7, 5, 9)
        sudoku.insert(7, 8, 5)

        sudoku.insert(8, 4, 8)
        sudoku.insert(8, 7, 7)
        sudoku.insert(8, 8, 9)

    def reset_board(self) -> None:

        for i in range(9):
            self.rows[i].clear()
            self.cols[i].clear()
            self.boxes[i].clear()

        for i in range(9):
            for j in range(9):
                self.board[i][j] = 0


sudoku = SudokuGrid()
sudoku.easy_preset()
sudoku.visualize()