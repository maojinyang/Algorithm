import sys
import time

from matplotlib import pyplot as plt

from utils import *

sys.setrecursionlimit(1000000)


def three_ways_partition(A, p, r):
    pt = p
    rt = r
    i = p + 1
    pivot = A[p]

    while i <= rt:
        if A[i] < pivot:
            A[i], A[pt] = A[pt], A[i]
            pt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[rt] = A[rt], A[i]
            rt -= 1
        else:
            i += 1
    return pt, rt


def quicksort(A, p, r):
    if p < r:
        pt, rt = three_ways_partition(A, p, r)
        quicksort(A, p, pt - 1)
        quicksort(A, rt + 1, r)


if __name__ == '__main__':
    DATA, ratios = Build_Data(42, 11)
    my_time_cost = []
    for data in DATA:
        start_time = time.time()
        quicksort(data, 0, len(data) - 1)
        end_time = time.time()
        # print(end_time - start_time)
        my_time_cost.append(end_time - start_time)

    python_time_cost = []
    for data in DATA:
        start_time = time.time()
        sorted(data)
        end_time = time.time()
        # print(end_time - start_time)
        python_time_cost.append(end_time - start_time)

    x_axis_data = ratios
    y_axis_data1 = my_time_cost
    y_axis_data2 = python_time_cost

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='my opt imp')
    plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='python imp')

    plt.legend()
    plt.xlabel('ratio')
    plt.ylabel('time')

    plt.show()

    # data = [2, 5, 8, 6, 4, 89, 96, 2, 4, 56, 6]
    # quicksort(data, 0, len(data)-1)
    # print(data)
