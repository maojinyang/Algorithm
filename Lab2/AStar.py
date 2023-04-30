import numpy as np
import heapq as hq
from utils import *


# start, end, map = Init_Map_1()
start, end, map = Init_Map_2()

map_x = len(map)
map_y = len(map[0])

open = []
close = []
hq.heapify(open)
hq.heappush(open, Node(nowx=start[0], nowy=start[1], dist=GetDist(start, end)))
PATH = None

while len(open) > 0:
    item = hq.heappop(open)
    nowx = item.nowx
    nowy = item.nowy

    if nowx < 0 or nowx >= map_x or nowy < 0 or nowy >= map_y:
        continue

    if map[nowx][nowy] == 3:
        continue

    if nowx == end[0] and nowy == end[1]:
        PATH = item.path
        break

    if Contain(close, [nowx, nowy]):
        continue

    close.append(item)

    newcost = item.cost + 1
    oblique_cost = item.cost + np.sqrt(2)
    if map[nowx][nowy] == 4:
        newcost += 4
        oblique_cost += 4
    elif map[nowx][nowy] == 8:
        newcost += 2
        oblique_cost += 2
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

visualization(map)
