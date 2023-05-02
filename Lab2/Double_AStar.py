import numpy as np
import heapq as hq
from utils import *

start, end, map = Init_Map_1()
# start, end, map = Init_Map_2()

map_x = len(map)
map_y = len(map[0])
obsindex = 3

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

visualization(map)
