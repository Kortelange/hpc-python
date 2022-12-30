import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GOL:
    #square game of life
    def __init__(self, size=4, board=None):
        if board is None:
            self.board = np.random.randint(0, 2, size=(size, size))
            self.size = size
        else:
            self.board = board
            self.size = board.shape[0]
        self.reset_neighbors()
        self.im = None
        self.anim = None

    def reset_neighbors(self):
        self.neighbors = np.zeros_like(self.board)

    def get_right_neighbors(self, column):
        right_neighbors = self.board[:, column + 1].copy()
        right_neighbors[:-1] += self.board[1:, column + 1]
        right_neighbors[1:] += self.board[:-1, column + 1]
        return right_neighbors

    def get_left_neighbors(self, column):
        left_neighbors = self.board[:, column - 1].copy()
        left_neighbors[:-1] += self.board[1:, column - 1]
        left_neighbors[1:] += self.board[: -1, column - 1]
        return left_neighbors

    def get_upper_neighbors(self, row):
        return self.board[row - 1, :].copy()

    def get_lower_neighbors(self, row):
        return self.board[row + 1, :].copy()

    def get_neighbours(self):
        self.reset_neighbors()
        neighbors = self.neighbors
        # get neighbors of first row, column
        neighbors[0, :] += self.get_lower_neighbors(0)
        neighbors[:, 0] += self.get_right_neighbors(0)
        # get neighbors of last row, column
        neighbors[-1, :] += self.get_upper_neighbors(-1)
        neighbors[:, -1] += self.get_left_neighbors(-1)

        # fill in last neighbors
        for i in range(1, self.size - 1):
            neighbors[i, :] += self.get_lower_neighbors(i)
            neighbors[i, :] += self.get_upper_neighbors(i)
            neighbors[:, i] += self.get_left_neighbors(i)
            neighbors[:, i] += self.get_right_neighbors(i)

    def update(self):
        self.get_neighbours()
        # handle zeroes
        zeroes = self.board == 0
        self.board[zeroes] += (self.neighbors[zeroes] == 3) * 1
        # handle ones
        ones = self.board == 1
        self.board[ones] -= (self.neighbors[ones] < 2) * 1
        self.board[ones] -= (self.neighbors[ones] > 3) * 1

    def play(self, maxiterations=500):
        for i in range(maxiterations):
            previous_board = self.board.copy()
            self.update()
            if (self.board == previous_board).all():
                break
        if i == maxiterations - 1:
            print('Solution is not complete')

    def animate(self, i):
        gol.update()
        self.im.set_data(gol.board)
        return self.im

    def create_animation(self, max_iterations=50):
        fig, (axl, axr) = plt.subplots(ncols=2)
        axl.imshow(self.board)
        self.im = axr.imshow(self.board)
        self.anim = animation.FuncAnimation(fig, self.animate, frames=max_iterations, interval=10)

    def play_animation(self, max_iterations=50):
        if not self.anim:
            self.create_animation(max_iterations)
        plt.show()



board = np.zeros((32, 32))
board[15, :] = 1
board[:, 15] = 1
gol = GOL(size=32, board=board)

gol.play_animation(100)