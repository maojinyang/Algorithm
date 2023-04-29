import datetime
import math
import utils


def polar_angle_distance_sort(points, polar_point):
    return sorted(points, key=lambda p: (math.atan2(p[1] - polar_point[1], p[0] - polar_point[0]), (p[0] - polar_point[0]) ** 2 + (p[1] - polar_point[1]) ** 2))


def Graham_Scan_Convex_Hull(points):
    start_time = datetime.datetime.now()

    left_bottom = utils.get_most_left_bottom_point(points)
    order_points = polar_angle_distance_sort(points, left_bottom)
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
    end_time = datetime.datetime.now()
    print("计算时间---", (end_time - start_time))
    return stack


def main():
    test_settings = [500]

    for test_num in test_settings:
        points = utils.generate_dots(test_num, seed=88)
        utils.draw_graph(points)

        points = Graham_Scan_Convex_Hull(points)
        utils.draw_graph(points)


if __name__ == '__main__':
    main()
