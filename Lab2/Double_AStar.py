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
    ['none', 'magenta', 'white', 'black', 'yellow', 'cyan', 'green', 'red', 'blue', 'purple'])

# 初始化open与close数组
openA = []
closeA = []
hq.heapify(openA)
hq.heappush(openA, Node(nowx=start[0], nowy=start[1], dist=GetDist(start, end)))
PATH_A = None

openB = []
closeB = []
hq.heapify(openB)
hq.heappush(openB, Node(nowx=end[0], nowy=end[1], dist=GetDist(end, start)))
PATH_B = None

while len(openA) > 0 and len(openB) > 0:
    item = hq.heappop(openA)
    nowx = item.nowx
    nowy = item.nowy

    if nowx < 0 or nowx >= map_x or nowy < 0 or nowy >= map_y:
        continue

    if map[nowx][nowy] == obsindex:
        continue

    if Contain(closeB, [nowx, nowy]):
        PATH_A = item.path
        for i in range(len(closeB)):
            if closeB[i].nowx == nowx and closeB[i].nowy == nowy:
                PATH_B = closeB[i].path
        break

    if Contain(closeA, [nowx, nowy]):
        continue

    # 当前节点加入close列表
    closeA.append(item)

    # 生成当前节点的下一步策略
    newcost = item.cost + 1
    oblique_cost = item.cost + np.sqrt(2)
    if map[nowx][nowy] == 4:
        newcost += 4
        oblique_cost += 4
    elif map[nowx][nowy] == 8:
        newcost += 2
        oblique_cost += 2
    hq.heappush(openA, Node(nowx=nowx + 1, nowy=nowy + 1, dist=GetDist([nowx + 1, nowy + 1], end), path=item.path + [[nowx + 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(openA, Node(nowx=nowx - 1, nowy=nowy + 1, dist=GetDist([nowx - 1, nowy + 1], end), path=item.path + [[nowx - 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(openA, Node(nowx=nowx - 1, nowy=nowy - 1, dist=GetDist([nowx - 1, nowy - 1], end), path=item.path + [[nowx - 1, nowy - 1]], cost=oblique_cost))
    hq.heappush(openA, Node(nowx=nowx + 1, nowy=nowy - 1, dist=GetDist([nowx + 1, nowy - 1], end), path=item.path + [[nowx + 1, nowy - 1]], cost=oblique_cost))

    hq.heappush(openA, Node(nowx=nowx + 1, nowy=nowy, dist=GetDist([nowx + 1, nowy], end), path=item.path + [[nowx + 1, nowy]], cost=newcost))
    hq.heappush(openA, Node(nowx=nowx, nowy=nowy + 1, dist=GetDist([nowx, nowy + 1], end), path=item.path + [[nowx, nowy + 1]], cost=newcost))
    hq.heappush(openA, Node(nowx=nowx - 1, nowy=nowy, dist=GetDist([nowx - 1, nowy], end), path=item.path + [[nowx - 1, nowy]], cost=newcost))
    hq.heappush(openA, Node(nowx=nowx, nowy=nowy - 1, dist=GetDist([nowx, nowy - 1], end), path=item.path + [[nowx, nowy - 1]], cost=newcost))

    item = hq.heappop(openB)
    nowx = item.nowx
    nowy = item.nowy

    if nowx < 0 or nowx >= map_x or nowy < 0 or nowy >= map_y:
        continue

    if map[nowx][nowy] == obsindex:
        continue

    if Contain(closeA, [nowx, nowy]):
        PATH_B = item.path
        for i in range(len(closeA)):
            if closeA[i].nowx == nowx and closeA[i].nowy == nowy:
                PATH_A = closeA[i].path
        break

    if Contain(closeB, [nowx, nowy]):
        continue

    # 当前节点加入close列表
    closeB.append(item)

    # 生成当前节点的下一步策略
    newcost = item.cost + 1
    oblique_cost = item.cost + np.sqrt(2)
    if map[nowx][nowy] == 4:
        newcost += 4
        oblique_cost += 4
    elif map[nowx][nowy] == 8:
        newcost += 2
        oblique_cost += 2
    hq.heappush(openB, Node(nowx=nowx + 1, nowy=nowy + 1, dist=GetDist([nowx + 1, nowy + 1], start), path=item.path + [[nowx + 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(openB, Node(nowx=nowx - 1, nowy=nowy + 1, dist=GetDist([nowx - 1, nowy + 1], start), path=item.path + [[nowx - 1, nowy + 1]], cost=oblique_cost))
    hq.heappush(openB, Node(nowx=nowx - 1, nowy=nowy - 1, dist=GetDist([nowx - 1, nowy - 1], start), path=item.path + [[nowx - 1, nowy - 1]], cost=oblique_cost))
    hq.heappush(openB, Node(nowx=nowx + 1, nowy=nowy - 1, dist=GetDist([nowx + 1, nowy - 1], start), path=item.path + [[nowx + 1, nowy - 1]], cost=oblique_cost))

    hq.heappush(openB, Node(nowx=nowx + 1, nowy=nowy, dist=GetDist([nowx + 1, nowy], start), path=item.path + [[nowx + 1, nowy]], cost=newcost))
    hq.heappush(openB, Node(nowx=nowx, nowy=nowy + 1, dist=GetDist([nowx, nowy + 1], start), path=item.path + [[nowx, nowy + 1]], cost=newcost))
    hq.heappush(openB, Node(nowx=nowx - 1, nowy=nowy, dist=GetDist([nowx - 1, nowy], start), path=item.path + [[nowx - 1, nowy]], cost=newcost))
    hq.heappush(openB, Node(nowx=nowx, nowy=nowy - 1, dist=GetDist([nowx, nowy - 1], start), path=item.path + [[nowx, nowy - 1]], cost=newcost))

print(PATH_A)
for i in PATH_A:
    map[i[0]][i[1]] = 1
print(PATH_B)
for i in PATH_B:
    map[i[0]][i[1]] = 5
map[start[0]][start[1]] = 5
map[end[0]][end[1]] = 6
plt.imshow(map, cmap=cmap, interpolation='nearest', vmin=0, vmax=7)
plt.show()
