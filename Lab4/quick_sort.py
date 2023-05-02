import time
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
    # random.seed(42)
    # data = [2, 1, 4, 3, 6]
    # quicksort(data, 0, len(data) - 1)
    # print(data)
    DATA = Build_Data(42)
    for data in DATA:
        start_time = time.time()
        quicksort(data, 0, len(data) - 1)
        # print(data)
        end_time = time.time()
        print(end_time - start_time)
