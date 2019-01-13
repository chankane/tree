import numpy as np
from numba import jit
import matplotlib.pyplot as plt


@jit
def _norm(pos_list: np.ndarray):
    dup_list = np.copy(pos_list)
    len_list = np.zeros(pos_list.shape[0])
    for i in range(1, len(pos_list)):
        local = dup_list[i] - dup_list[i // 2]
        e = np.linalg.norm(local)
        len_list[i] = len_list[i // 2] + e
        if len_list[i] > 1:
            local *= (1 - len_list[i // 2]) / e
            dup_list[i] = dup_list[i // 2] + local
            len_list[i] = 1
    return dup_list


@jit
def _cre_rand_pos_list(size):
    data = np.random.rand(size, 2)
    data -= 0.5
    data[0] = [0, 0]
    return data


@jit
def _plot(pos_list: np.ndarray, col: str = "r", mar: str = "o"):
    for i in range(1, len(pos_list)):
        x = np.array([pos_list[i][0], pos_list[i // 2][0]])
        y = np.array([pos_list[i][1], pos_list[i // 2][1]])
        plt.plot(x, y, color=col, marker=mar)


def main():
    # plt.plot((0, 1), (0, 1))
    # plt.show()

    data = _cre_rand_pos_list(2**3)
    # data = np.zeros((2**3, 2))

    """
    data = np.array([
        [0, 0],
        [0, 0.5],
        [0.8, 1.6],
        [-0.8, 0.5],
    ])
    """

    """
    data = np.array([
        [0., 0.],
        [2., 2.]
    ])
    """
    #print(_norm(data))
    # print(_calc_leaf_pos((0, 0), data))
    # print(_calc_pos_list(0, data))
    # _plot(_calc_pos_list(0, data))
    plt.axes().set_aspect('equal', 'datalim')
    plt.grid(True)
    # plt.show()
    # plt.grid(True)
    _plot(data)
    _plot(_norm(data), "g", "x")
    plt.show()


if __name__ == "__main__":
    main()
