# 迷宫问题

```python
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1),
]


def maze_path_queue(x1: int, y1: int, x2: int, y2: int):
    """
    走出迷宫，采用bfs广度优先搜索。
    时间复杂度: O(n)
    空间复杂度: O(n)

    :param x1: 入口x
    :param y1: 入口y
    :param x2: 出口x
    :param y2: 出口y
    :return: [] 踪迹
    """

    def print_r(path_):
        """
        打印路径
        :param path_: 走过的路径
        :return:
        """
        # 最后一个节点
        cur_node_ = path_[-1]
        #
        real_path = []
        # 到起点结束
        while cur_node_[2] != -1:
            # 记录路径
            real_path.append(cur_node_[0:2])
            # 走过了哪些
            cur_node_ = path_[cur_node_[2]]
        # 记录起点
        real_path.append(cur_node_[0:2])
        # 反转
        real_path.reverse()
        for node in real_path:
            # 打印路径
            print(node)

    # 创建队列
    queue = collections.deque()
    # 添加初始值，也就是起点
    queue.append((x1, y1, -1))
    # 记录走过的路径
    path = []
    while queue:
        # 获取当前走到的点位
        cur_node = queue.popleft()
        # 记录走过的点位
        path.append(cur_node)
        # 如果到达出口则结束
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return True
        # 上下左右四个方向行走
        for dir in dirs:
            # 下一步
            next_node = dir(cur_node[0], cur_node[1])
            # 是否可以走
            if maze[next_node[0]][next_node[1]] == 0:
                # 可以走则记录，继续走
                queue.append((next_node[0], next_node[1], len(path) - 1))
                # 标记已经走过的
                maze[next_node[0]][next_node[1]] = 3
    print("没有路")
    return False


if __name__ == "__main__":
    maze_path_queue(1, 1, 8, 8)
```



