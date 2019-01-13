import numpy as np
from numba import jit


@jit
def _cre_rand_pos_list(size):
    data = np.random.rand(size, 2) * 2
    data -= 1
    data[0] = [0, 0]
    return data


arr = _cre_rand_pos_list(8)

len_list = np.zeros(arr.shape[0])
for i in range(1, len(arr)):
    len_list[i] = \
        np.linalg.norm(arr[i // 2]) + np.linalg.norm(arr[i])

print(len_list)
