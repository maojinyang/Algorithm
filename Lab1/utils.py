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


def get_most_left_bottom_point(points):
    left_bottom = sorted(points, key=lambda p: (p[0], p[1]))[0]
    return left_bottom


def rearrange_points(points):
    sorted(points, key=lambda p: (p[0], p[1]))
    return points


def draw_performance_graph():
    pass


# if __name__ == '__main__':
#     dot_list = generate_dots(10000)
#     print(dot_list)
