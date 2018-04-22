import itertools

SIZE = 50


class Life:
    def __init__(self):
        self.grid = [[False for _ in range(SIZE)] for _ in range(SIZE)]

    def iterate(self):
        next_gen = [[False for _ in range(SIZE)] for _ in range(SIZE)]
        for i, j in itertools.product(range(SIZE), repeat=2):
            cell = self.grid[i][j]
            up = down = left = right = upper_left = upper_right = lower_left = lower_right = False

            if i > 0:
                up = self.grid[i-1][j]
            if j > 0:
                left = self.grid[i][j-1]
            if i < SIZE - 1:
                down = self.grid[i+1][j]
            if j < SIZE - 1:
                right = self.grid[i][j+1]
            if i > 0 and j > 0:
                upper_left = self.grid[i-1][j-1]
            if i > 0 and j < SIZE-1:
                upper_right = self.grid[i-1][j+1]
            if i < SIZE-1 and j > 0:
                lower_left = self.grid[i+1][j-1]
            if i < SIZE-1 and j < SIZE-1:
                lower_right = self.grid[i+1][j+1]

            neighbors = (up, down, left, right, upper_left, upper_right, lower_left, lower_right)

            if cell and neighbors.count(True) in (2, 3):
                next_gen[i][j] = True
            if not cell and neighbors.count(True) == 3:
                next_gen[i][j] = True

        self.grid = next_gen

    def change_life(self, x: int, y: int) -> None:
        self.grid[y][x] = not self.grid[y][x]
