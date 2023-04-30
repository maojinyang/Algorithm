import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import heapq as hq


# 搜索节点
class Node(object):
    def __init__(self, nowx=0, nowy=0, cost=0, dist=0, path=None) -> None:
        if path is None:
            path = []
        self.nowx = nowx
        self.nowy = nowy
        self.cost = cost
        self.dist = dist
        self.path = path

    def __lt__(self, other):
        return self.dist + self.cost < other.dist + other.cost

    def __le__(self, other):
        return self.dist + self.cost <= other.dist + other.cost

    def __gt__(self, other):
        return self.dist + self.cost > other.dist + other.cost

    def __ge__(self, other):
        return self.dist + self.cost >= other.dist + other.cost

    def __eqeq__(self, other):
        return self.dist + self.cost == other.dist + other.cost

    def __ne__(self, other):
        return self.dist + self.cost != other.dist + other.cost


# 求距离
def GetDist(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])
    # return (abs(end[0] - start[0]) ** 2 + abs(end[1] - start[1]) ** 2) ** 0.5


def Contain(list, point):
    for i in range(len(list)):
        if list[i].nowx == point[0] and list[i].nowy == point[1]:
            return True


def Reverse_Path():
    pass


# 产生地图矩阵
# start = [8, 3]
# end = [9, 14]
# map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = [10, 4]
end = [0, 35]
map = [[0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4],
       [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4],
       [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 8, 8, 0, 0, 0, 0, 0],
       [0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 8, 8, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 3, 0, 0, 0],
       [0, 0, 3, 0, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 8, 8, 0, 8, 8, 0, 0, 0],
       [0, 0, 3, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 0, 8, 8, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 0, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 8, 8, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

map_x = len(map)
map_y = len(map[0])
obsindex = 3

cmap = colors.ListedColormap(
    ['none', 'magenta', 'white', 'black', 'yellow', 'cyan', 'green', 'red', 'blue'])

# 初始化open与close数组
open = []
close = []
hq.heapify(open)
hq.heappush(open, Node(nowx=start[0], nowy=start[1], dist=GetDist(start, end)))
PATH = None
# 搜索路径
while len(open) > 0:
    item = hq.heappop(open)
    nowx = item.nowx
    nowy = item.nowy

    # 避免超出地图界限
    if nowx < 0 or nowx >= map_x or nowy < 0 or nowy >= map_y:
        continue

    # 避开障碍
    if map[nowx][nowy] == obsindex:
        continue

    # # 标记地图
    # map[nowx][nowy] = 1

    # 搜索到终点
    if nowx == end[0] and nowy == end[1]:
        PATH = item.path
        break

    # 取出的节点已经在close列表里面则不在使用
    if Contain(close, [nowx, nowy]):
        continue

    # 当前节点加入close列表
    close.append(item)

    # 生成当前节点的下一步策略
    newcost = item.cost + 1
    oblique_cost = item.cost + np.sqrt(2)
    hq.heappush(open, Node(nowx=nowx + 1, nowy=nowy + 1, dist=GetDist([nowx + 1, nowy + 1], end), path=item.path + [[nowx + 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(open, Node(nowx=nowx - 1, nowy=nowy + 1, dist=GetDist([nowx - 1, nowy + 1], end), path=item.path + [[nowx - 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(open, Node(nowx=nowx - 1, nowy=nowy - 1, dist=GetDist([nowx - 1, nowy - 1], end), path=item.path + [[nowx - 1, nowy - 1]], cost=oblique_cost))
    hq.heappush(open, Node(nowx=nowx + 1, nowy=nowy - 1, dist=GetDist([nowx + 1, nowy - 1], end), path=item.path + [[nowx + 1, nowy - 1]], cost=oblique_cost))

    hq.heappush(open, Node(nowx=nowx + 1, nowy=nowy, dist=GetDist([nowx + 1, nowy], end), path=item.path + [[nowx + 1, nowy]], cost=newcost))
    hq.heappush(open, Node(nowx=nowx, nowy=nowy + 1, dist=GetDist([nowx, nowy + 1], end), path=item.path + [[nowx, nowy + 1]], cost=newcost))
    hq.heappush(open, Node(nowx=nowx - 1, nowy=nowy, dist=GetDist([nowx - 1, nowy], end), path=item.path + [[nowx - 1, nowy]], cost=newcost))
    hq.heappush(open, Node(nowx=nowx, nowy=nowy - 1, dist=GetDist([nowx, nowy - 1], end), path=item.path + [[nowx, nowy - 1]], cost=newcost))


print(PATH)
for i in PATH:
    map[i[0]][i[1]] = 1
map[start[0]][start[1]] = 5
map[end[0]][end[1]] = 6
plt.imshow(map, cmap=cmap, interpolation='nearest', vmin=0, vmax=7)
plt.show()
