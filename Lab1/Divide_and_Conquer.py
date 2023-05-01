import datetime
import time

from matplotlib import pyplot as plt

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
    start = time.time()
    order_points = utils.rearrange_points(points)
    left = order_points[0]
    right = order_points[-1]
    convex_points = []
    get_upper_point(left, right, order_points, convex_points)
    get_bottom_point(left, right, order_points, convex_points)
    convex_points.append(left)
    convex_points.append(right)
    end = time.time()
    print(end - start)
    return convex_points, end - start


def main():
    test_settings = [100, 500, 1000, 2000, 3000]

    run_times = []
    for test_num in test_settings:
        points = utils.generate_dots(test_num, seed=88)
        convex_points, runtime = Divide_and_Conquer(points)
        # convex_points = utils.polar_angle_distance_sort(convex_points, convex_points[0])
        # utils.draw(points, convex_points)
        run_times.append(runtime)
    plt.plot(test_settings, run_times)
    plt.show()


if __name__ == '__main__':
    main()
