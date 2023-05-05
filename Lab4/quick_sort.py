import time

from matplotlib import pyplot as plt

from utils import *
import sys

sys.setrecursionlimit(1000000)


def random_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]

    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def partition(A, p, r):
    x = A[p]
    i1 = p
    i2 = r

    while True:
        while A[i1] <= x and i1 < r:
            i1 += 1
        while A[i2] >= x and i2 > p:
            i2 -= 1
        if i1 >= i2:
            break
        else:
            A[i1], A[i2] = A[i2], A[i1]
    A[p], A[i2] = A[i2], A[p]
    mid = i2
    return mid


def quicksort(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def quicksort_tail(A, p, r):
    while p < r:
        i = random_partition(A, p, r)
        if i - p < r - i:
            quicksort_tail(A, p, i - 1)
            p = i + 1
        else:
            quicksort_tail(A, i + 1, r)
            r = i - 1


if __name__ == '__main__':
    DATA, ratios = Build_Data(42, 2)

    # my_time_cost = [3.783, 439.511]
    my_time_cost = []
    for data in DATA:
        start_time = time.time()
        quicksort_tail(data, 0, len(data) - 1)
        end_time = time.time()
        print(end_time - start_time)
        my_time_cost.append(end_time - start_time)

    python_time_cost = []
    for data in DATA:
        start_time = time.time()
        sorted(data)
        end_time = time.time()
        print(end_time - start_time)
        python_time_cost.append(end_time - start_time)

    x_axis_data = ratios
    y_axis_data1 = my_time_cost
    y_axis_data2 = python_time_cost

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='my imp')  # '
    plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='python imp')

    plt.legend()
    plt.xlabel('ratio')
    plt.ylabel('time')

    plt.show()
