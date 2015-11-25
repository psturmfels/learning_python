class Board(object):
    """
    A class used to represent a 10x10 grid of characters. Specifically,
    this class was designed to represent a player's board in battleship.
    """
    def __init__(self):
        self.num_rows = 10
        self.num_cols = 10
        self.grid = [['*' for x in range(self.num_cols)] for x in range(self.num_rows)]

    def print_grid(self):
        print("  ", end="")
        for x in range(self.num_cols):
            print(x, end=" ")
        print()

        for row in range(self.num_rows):
            print(row, end=" ")
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def set_coord(self, row_coord, col_coord, character):
        if 0 <= row_coord < self.num_rows and 0 <= col_coord < self.num_cols:
            self.grid[row_coord][col_coord] = character


class Player(object):
    """
    The highest level class in a tree of classes designed to represent various
    types of battleship players. Subclasses are HumanPlayer and SimplePlayer.
    """
    def __init__(self, name_in):
        self.name = name_in
        self.board = Board()
        self.ships = [[], [], [], []]


class HumanPlayer(Player):
    """
    Inherits from Player. Designed to model a human player of battleship.
    """
    def __init__(self, name_in):
        self.my_board = Board()
        super(HumanPlayer, self).__init__(name_in)

    # Need to fix: A player can currently overwrite his/her previously set ships
    # When positioning the later ones. Make sure a player cannot do this.
    def position_ships(self):

        print("Your current board:")
        self.my_board.print_grid()
        print()
        print("You have 4 ships of lengths 2, 3, 4 and 5 respectively.")

        for index, ship in enumerate(self.ships):
            print()
            print("Ship number " + str(index + 1) + " [length " + str(index + 2) + "]:")

            does_conflict = True
            while does_conflict:
                ship_direction = int(input("  Enter a ship orientation [0 for downwards, 1 for rightwards]: "))
                while ship_direction != 0 and ship_direction != 1:
                    print("  Invalid ship direction. Valid ship directions are 0 and 1.")
                    ship_direction = int(input("  Enter a ship orientation [0 for downwards, 1 for rightwards]: "))

                ship_col = int(input("  Enter the initial column for the ship: "))

                if ship_direction == 0:
                    while ship_col < 0 or ship_col > 9:
                        print("  Invalid ship column. Valid column choices are 0 - 9.")
                        ship_col = int(input("  Enter the initial column for the ship: "))
                else:
                    while ship_col < 0 or ship_col > (9 - index - 1):
                        print("  Invalid ship column. Valid column choices are 0 - " + str(9 - index - 1) + ".")
                        ship_col = int(input("  Enter the initial column for the ship: "))

                ship_row = int(input("  Enter the initial row for the ship: "))

                if ship_direction == 1:
                    while ship_row < 0 or ship_row > 9:
                        print("  Invalid ship column. Valid column choices are 0 - 9.")
                        ship_col = int(input("  Enter the initial row for the ship: "))
                else:
                    while ship_row < 0 or ship_row > (9 - index - 1):
                        print("  Invalid ship row. Valid row choices are 0 - " + str(9 - index - 1) + ".")
                        ship_row = int(input("  Enter the initial row for the ship: "))

                if ship_direction == 0:
                    for row in range(ship_row, ship_row + index + 2):
                        conflict_coordinate = [row, ship_col, self.my_board.grid[row][ship_col]]
                        does_conflict = conflict_coordinate[2] != '*'

                        if does_conflict:
                            print("  This ship would intersect with ship " + str(conflict_coordinate[2]) +
                                  " at coordinate (" + str(conflict_coordinate[0]) + ", " + str(conflict_coordinate[1]) + ")")
                            break
                else:
                    for col in range(ship_col, ship_col + index + 2):
                        conflict_coordinate = [ship_row, col, self.my_board.grid[ship_row][col]]
                        does_conflict = conflict_coordinate[2] != '*'

                        if does_conflict:
                            print("  This ship would intersect with ship " + str(conflict_coordinate[2]) +
                                  " at coordinates (" + str(conflict_coordinate[0]) + ", " + str(conflict_coordinate[1]) + ")")
                            break



            self.ships[index] = [ship_direction, ship_row, ship_col, index + 2]

            if ship_direction == 0:
                for row in range(ship_row, ship_row + index + 2):
                    self.my_board.set_coord(row, ship_col, str(index + 2))
            else:
                for col in range(ship_col, ship_col + index + 2):
                    self.my_board.set_coord(ship_row, col, str(index + 2))

            print()
            print("Your current board:")
            self.my_board.print_grid()


class SimplePlayer(Player):
    """
    Inherits from Player. Designed to model a simple AI playing battleship.
    """
    def __init__(self, name_in):
        super(SimplePlayer, self).__init__(name_in)

drew_human = HumanPlayer("Drew")
drew_human.position_ships()
print()
