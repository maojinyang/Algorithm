import time

from matplotlib import pyplot as plt

import utils


def Graham_Scan_Convex_Hull(points):
    start = time.time()

    left_bottom = utils.get_most_left_bottom_point(points)
    order_points = utils.polar_angle_distance_sort(points, left_bottom)
    order_points.remove(left_bottom)

    stack = [left_bottom, order_points[0]]
    for i in range(1, len(order_points)):
        if len(stack) < 2:
            stack.append(order_points[i])

        else:
            while len(stack) >= 2:
                cross = (stack[-1][0] - stack[-2][0]) * (order_points[i][1] - stack[-2][1]) - (order_points[i][0] - stack[-2][0]) * (stack[-1][1] - stack[-2][1])
                if cross <= 0:
                    stack.pop()
                else:
                    stack.append(order_points[i])
                    break
    end = time.time()
    print(end - start)
    return stack, end - start


def main():
    # test_settings = [50, 100, 200]
    test_settings = [100, 500, 1000, 2000, 3000]

    run_times = []
    for test_num in test_settings:
        points = utils.generate_dots(test_num, seed=88)
        convex_points, runtime = Graham_Scan_Convex_Hull(points)
        # utils.draw(points, convex_points)
        run_times.append(runtime)
    plt.plot(test_settings, run_times)
    plt.show()


if __name__ == '__main__':
    main()
