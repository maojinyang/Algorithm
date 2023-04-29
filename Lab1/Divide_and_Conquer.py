import datetime

import utils
import sys

sys.setrecursionlimit(100000)


def get_upper_point(left, right, points, convex_points):
    max_area = 0
    max_point = None
    for point in points:
        if point == left or point == right:
            continue
        cur_area = utils.calc_triangle_area(left, right, point)
        if cur_area > max_area:
            max_point = point
            max_area = cur_area
    if max_area != 0:
        convex_points.append(max_point)
        get_upper_point(left, max_point, points, convex_points)
        get_upper_point(max_point, right, points, convex_points)


def get_bottom_point(left, right, points, convex_points):
    max_area = 0
    max_point = None
    for point in points:
        if point == left or point == right:
            continue
        cur_area = utils.calc_triangle_area(left, right, point)
        if cur_area < max_area:
            max_point = point
            max_area = cur_area
    if max_area != 0:
        convex_points.append(max_point)
        get_bottom_point(left, max_point, points, convex_points)
        get_bottom_point(max_point, right, points, convex_points)


def Divide_and_Conquer(points):
    start_time = datetime.datetime.now()
    order_points = utils.rearrange_points(points)
    left = order_points[0]
    right = order_points[-1]
    convex_points = []
    get_upper_point(left, right, order_points, convex_points)
    get_bottom_point(left, right, order_points, convex_points)
    convex_points.append(left)
    convex_points.append(right)
    end_time = datetime.datetime.now()
    print("计算时间---", (end_time - start_time))
    return convex_points


def main():
    test_settings = [50]

    for test_num in test_settings:
        points = utils.generate_dots(test_num, seed=88)
        convex_points = Divide_and_Conquer(points)
        convex_points = utils.polar_angle_distance_sort(convex_points, convex_points[0])
        utils.draw(points, convex_points)


if __name__ == '__main__':
    main()
