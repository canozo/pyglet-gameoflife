import itertools


class Life:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[False for _ in range(self.size)] for _ in range(self.size)]

    def iterate(self):
        next_gen = [[False for _ in range(self.size)] for _ in range(self.size)]
        for i, j in itertools.product(range(self.size), repeat=2):
            s = self.size
            cell = self.grid[i][j]

            up = self.grid[i-1][j]
            left = self.grid[i][j-1]
            down = self.grid[(i+1) % s][j]
            right = self.grid[i][(j+1) % s]
            upper_left = self.grid[i-1][j-1]
            upper_right = self.grid[i-1][(j+1) % s]
            lower_left = self.grid[(i+1) % s][j-1]
            lower_right = self.grid[(i+1) % s][(j+1) % s]

            neighbors = (up, down, left, right, upper_left, upper_right, lower_left, lower_right)

            if cell and neighbors.count(True) in (2, 3):
                next_gen[i][j] = True
            if not cell and neighbors.count(True) == 3:
                next_gen[i][j] = True

        self.grid = next_gen

    def change_life(self, x: int, y: int) -> None:
        self.grid[y][x] = not self.grid[y][x]
