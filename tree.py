import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from cmath import rect


@jit
def _calc_leaf_pos(root_pos, data):
    pos_list = np.zeros(data.shape[0], np.complex64)
    print(pos_list)
    # pos_list[0] = self.__pos
    for i in range(1, len(data)):
        vec = rect(data[i][0], data[i][1])
        pos_list[i] = pos_list[i // 2] + vec

    return pos_list[(len(data) - 1) // 2 + 1:]


@jit
def _calc_pos_list(root_pos, data):
    total = data.copy()
    pos_list = np.zeros(data.shape[0], np.complex64)
    pos_list[0] = root_pos
    for i in range(1, len(data)):
        pos_list[i] = pos_list[i // 2] + rect(data[i][0], data[i][1])

    return pos_list


@jit
def _plot(pos_list: np.ndarray):
    for i in range(1, len(pos_list)):
        x = np.array([pos_list[i].real, pos_list[i // 2].real])
        y = np.array([pos_list[i].imag, pos_list[i // 2].imag])
        plt.plot(x, y, color="m", marker="x")


def eval(data):
    self.__data = data


def main():
    plt.grid(True)
    # plt.plot((0, 1), (0, 1))
    # plt.show()

    # data = np.tile(np.array([0.2, np.pi / 3]), (8, 1))
    data = np.array([
        [0, 0],
        [0.2, 0],
        [0.2, np.pi / 3], [0.2, -np.pi / 3],
        [0.2, np.pi / 3], [0.2, -np.pi / 3],
        [0.2, np.pi / 3], [0.2, -np.pi / 3],
    ])
    # print(data)
    # print(_calc_leaf_pos((0, 0), data))
    print(_calc_pos_list(0, data))
    _plot(_calc_pos_list(0, data))
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()
    return 0


if __name__ == "__main__":
    main()
