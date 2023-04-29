import datetime

import utils
import sys

sys.setrecursionlimit(100000)  # 例如这里设置为十万


def dealleft(first, final, lis, temp):
    # temp用来标记位于凸包上的点
    max = 0
    index = -1
    # 处理first到final的上方，得到使first，final，i 三点组成的三角形面积最大的点i
    if first < final:
        for i in range(first, final):
            # 获得first，final，i 的坐标
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            # 计算first，final，i 三点组成的三角形面积
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i
    # 处理first到final的下方，得到使first，final，i 三点组成的三角形面积最大的点i
    else:
        for i in range(final, first):
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i

    if index != -1:
        temp[index] = 1
        dealleft(first, index, lis, temp)
        dealleft(index, final, lis, temp)


def Divide_and_Conquer(points):
    start_time = datetime.datetime.now()
    temp = {}
    result = []
    n = len(points)
    for i in range(n):
        temp[i] = 0
    order_points = utils.rearrange_points(points)
    temp[0] = 1
    temp[n - 1] = 1
    dealleft(0, n - 1, order_points, temp)
    dealleft(n - 1, 0, order_points, temp)
    for i in temp:
        if temp[i]:
            result.append(order_points[i])
    end_time = datetime.datetime.now()
    print("计算时间---", (end_time - start_time))
    return result


def main():
    test_settings = [50]

    for test_num in test_settings:
        points = utils.generate_dots(test_num, seed=88)
        utils.draw_graph(points)

        points = Divide_and_Conquer(points)
        utils.draw_graph(points)


if __name__ == '__main__':
    main()
