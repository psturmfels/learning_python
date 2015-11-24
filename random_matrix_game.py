import random
random.seed(1231)

class board:
    def __init__(self, num_rows_in, num_cols_in):
        self.grid = [['O' for x in xrange(num_cols_in)] for x in xrange(num_rows_in)]
        self.num_rows = num_rows_in
        self.num_cols = num_cols_in
        self.target_row = random.randrange(num_rows_in)
        self.target_column = random.randrange(num_cols_in)
        #self.grid[self.target_row][self.target_column] = 'X'

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print self.grid[row][column],
            print

    def make_guess(self, input_row, input_col):
        if input_row == self.target_row and input_col == self.target_column:
            self.grid[input_row][input_col] = '8'
            self.print_grid()
            print("Congratulations! You found the 8.")
            return True
        elif 0 <= input_row < self.num_rows and 0 <= input_col < self.num_cols:
            if self.grid[input_row][input_col] == 'X':
                print("You've already guessed that!")
            else:
                self.grid[input_row][input_col] = 'X'
                self.print_grid()
        else:
            print("Coordinate (" + str(input_row) + ", " + str(input_col) + ") is not in range.\n")
        return False


test_board = board(5, 5)
print("5x5 board initialized.")
row = input("Enter a row: ")
column = input("Enter a column: ")

while not test_board.make_guess(row, column):
    row = input("Enter a row: ")
    column = input("Enter a column: ")


