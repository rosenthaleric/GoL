import random as rnd
import pyglet
from cell import Cell


class GoL:

    def __init__(self, width, height, res):
        self.cols = int(width / res)
        self.rows = int(height / res)
        self.res = res
        self.cells = []
        self.next = []
        self.spawn = 0.5
        self.total = 0
        self.av_age = 0
        self.generate_cells()

    def generate_cells(self):
        for row in range(0, self.rows):
            self.cells.append([])
            self.next.append([])
            for col in range(0, self.cols):
                # array within array represents one row
                if rnd.random() < self.spawn:
                    self.cells[row].append(Cell(True))
                    self.next[row].append(Cell(True))
                    self.total += 1
                else:
                    self.cells[row].append(Cell(False))
                    self.next[row].append(Cell(False))

    def draw(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.cells[row][col].alive:
                    squareCoords = (col * self.res, row * self.res,
                                    col * self.res, row * self.res + self.res,
                                    col * self.res + self.res, row * self.res,
                                    col * self.res + self.res, row * self.res + self.res)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                 [0, 1, 2, 1, 2, 3],
                                                 ('v2i', squareCoords),
                                                 ('c3B', self.cells[row][col].age_color))

    def next_gen(self):
        age_sum = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                old = self.cells[row][col]
                neighbors = self.count_neighbors(row, col)
                if not old.alive and neighbors == 3:
                    self.next[row][col].set_alive(True)
                    self.total += 1
                elif old.alive and (neighbors > 3 or neighbors < 2):
                    self.next[row][col].set_alive(False)
                    self.total -= 1

        # important for aging
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.cells[row][col].set_alive(self.next[row][col].alive)
                age_sum += self.cells[row][col].aging()

        if self.total > 0:
            self.av_age = age_sum / self.total

    def count_neighbors(self, x, y):
        sum = -1 if self.cells[x][y].alive else 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # avoid out of bounce by wrapping around the edges
                # modulo remainder is either x+i or the wrapped around value
                row = (x + i + self.rows) % self.rows
                col = (y + j + self.cols) % self.cols
                sum += 1 if self.cells[row][col].alive else 0

        return sum

    def populate(self, col, row):
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = (row + i + self.rows) % self.rows
                col = (col + j + self.cols) % self.cols
                self.total += 1 if not self.next[row][col].alive else 0
                self.cells[row][col].set_alive(True)
