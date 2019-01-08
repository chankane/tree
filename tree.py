import matplotlib.pyplot as plt
import node as nd


class Tree:
    @staticmethod
    def __plot_line(start, end):
        plt.plot([start[0], end[0]], [start[1], end[1]], color="m")

    @staticmethod
    def __plot(root):
        for e in root.children:
            Tree.__plot_line(root.data, e.data)
            Tree.__plot(e)

    @staticmethod
    def __create(pos, depth):
        tmp = nd.Node(pos, [])
        if depth <= 0:
            return tmp

        # for i in range(2):
        tmp.children.append(Tree.__create([pos[0] - 1, pos[1] + 1], depth - 1))
        tmp.children.append(Tree.__create([pos[0] + 1, pos[1] + 1], depth - 1))

        return tmp

    def __init__(self, depth):
        self.__root = self.__create([0, 0], depth)
        plt.grid(True)

    def set_offset(self, offset):
        self.__root.data = offset

    def draw(self):
        Tree.__plot(self.__root)
        plt.show()
