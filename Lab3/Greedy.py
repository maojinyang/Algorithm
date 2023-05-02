import time

from matplotlib import pyplot as plt

from utils import *


def Run_Greedy(All_Set, Sub_Set):
    start = time.time()
    select = []
    while len(All_Set) != 0:
        select_item = None
        max_length = -1
        for item in Sub_Set:
            intersection = list(set(item) & set(All_Set))  # 求交集
            if len(intersection) > max_length:
                max_length = len(intersection)
                select_item = item
        All_Set = list(set(All_Set) - set(select_item))  # 求差集
        select.append(select_item)
    print(select)

    # 记录运行时间
    end = time.time()
    t = end - start
    print("运行时间", t)

    return t


def main():
    time_cost = []
    tests = [100, 1000, 5000]
    for i in tests:
        All_Set, Sub_Set = Build_Input(i)
        t = Run_Greedy(All_Set, Sub_Set)
        time_cost.append(t)
    plt.plot(tests, time_cost)
    plt.show()


if __name__ == '__main__':
    main()
