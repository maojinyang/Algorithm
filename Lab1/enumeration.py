from tqdm import tqdm

import utils


def is_point_inside_triangle(point, A, B, C):
    """
    判断点(px, py)是否在三角形ABC内部
    """
    px, py = point[0], point[1]
    ax, ay = A[0], A[1]
    bx, by = B[0], B[1]
    cx, cy = C[0], C[1]
    # 计算三角形ABC的面积
    ABC = abs((bx - ax) * (cy - ay) - (cx - ax) * (by - ay)) / 2
    # 计算三个子三角形的面积并求和
    ABP = abs((bx - ax) * (py - ay) - (px - ax) * (by - ay)) / 2
    APC = abs((cx - ax) * (py - ay) - (px - ax) * (cy - ay)) / 2
    PBC = abs((cx - bx) * (py - by) - (px - bx) * (cy - by)) / 2
    total = ABP + APC + PBC
    # 判断是否在三角形内部
    return total == ABC


def enumeration_convex_hull(points):
    is_convex = [True for _ in range(len(points))]
    for i in tqdm(range(len(points))):
        if not is_convex[i]:
            continue
        for j in range(len(points)):
            if not is_convex[j] or j == i:
                continue
            for k in range(len(points)):
                if not is_convex[k] or k == i or k == j:
                    continue
                for g in range(len(points)):
                    if not is_convex[g] or g == i or g == j or g == k:
                        continue
                    if is_point_inside_triangle(points[i], points[j], points[k], points[g]):
                        is_convex[i] = False
    result = []
    for point, convex in zip(points, is_convex):
        if convex:
            result.append(point)
    return result


if __name__ == '__main__':

    test_settings = [100]

    for test_num in test_settings:
        dots = utils.generate_dots(test_num)
        utils.draw_graph(dots)

        dots = enumeration_convex_hull(dots)
        utils.draw_graph(dots)
