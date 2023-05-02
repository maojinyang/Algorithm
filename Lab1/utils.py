import math
import random

from matplotlib import pyplot as plt


def generate_dots(num: int, seed=42):
    """
    生成2D正方形平面点集合，默认边长为100
    :param seed: 随机种子
    :param num: 数目
    :return: 点集合
    """
    dots = set()
    random.seed(seed)
    while len(dots) < num:
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        dots.add((x, y))
    return list(dots)


def draw(list_points, list_borders):
    """
    画图
    :param list_points: 所有点集
    :param list_borders: 所有边界点集
    :return: picture
    """
    list_all_x = []
    list_all_y = []
    for item in list_points:
        a, b = item
        list_all_x.append(a)
        list_all_y.append(b)
    list_borders.append(list_borders[0])
    for i in range(len(list_borders) - 1):
        one_, oneI = list_borders[i]
        two_, twoI = list_borders[i + 1]
        plt.plot([one_, two_], [oneI, twoI])
    plt.scatter(list_all_x, list_all_y)
    plt.show()


def draw_graph(points):
    # 将所有 x, y 坐标分别存储到两个列表中
    xs, ys = zip(*points)
    # 绘制点集
    plt.plot(xs, ys, 'o')
    # 设置图像标题和轴标签等
    plt.title("Point Set")
    plt.xlabel("X")
    plt.ylabel("Y")
    # 显示图像
    plt.show()


def polar_angle_distance_sort(points, polar_point):
    return sorted(points, key=lambda p: (math.atan2(p[1] - polar_point[1], p[0] - polar_point[0]), (p[0] - polar_point[0]) ** 2 + (p[1] - polar_point[1]) ** 2))


def get_most_left_bottom_point(points):
    left_bottom = sorted(points, key=lambda p: (p[0], p[1]))[0]
    return left_bottom


def rearrange_points(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))
    return points


def calc_triangle_area(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return x1 * y2 + x3 * y1 + x2 * y3 - x3 * y2 - x2 * y1 - x1 * y3


def draw_performance_graph():
    x_axis_data = [100, 500, 1000, 2000, 3000]
    # y_axis_data1 = [0.017, 1.235, 5.506, 15.024, 24.432]
    y_axis_data2 = [0.0, 0.001, 0.002, 0.004, 0.006]
    y_axis_data3 = [0.0, 0.005, 0.011, 0.022, 0.044]

    # 画图
    # plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='enumeration')  # '
    plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='graham scan')
    plt.plot(x_axis_data, y_axis_data3, 'go--', alpha=0.5, linewidth=1, label='divide and conquer')

    plt.legend()
    plt.xlabel('number')
    plt.ylabel('time')

    plt.show()


if __name__ == '__main__':
    draw_performance_graph()
