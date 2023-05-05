import time

import pulp
from matplotlib import pyplot as plt

from utils import Build_Input


def Run_LP(All_Set, Sub_Set):
    start = time.time()

    n = len(All_Set)

    # 目标函数：min CX  C取值为1
    # 约束条件：AX>=B
    freq = [0] * n
    C = [1] * n
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(All_Set)):
        for j in range(len(Sub_Set)):
            if All_Set[i] in Sub_Set[j]:
                A[i][j] = A[i][j] + 1
                freq[i] += 1
    max_f = max(freq)
    B = [1] * n

    # 定义X
    X = [pulp.LpVariable(f'x{i}', lowBound=0, upBound=1) for i in range(n)]

    # 确定最大化最小化问题，最大化只要把Min改成Max即可
    m = pulp.LpProblem(sense=pulp.LpMinimize)
    m += pulp.lpDot(C, X)

    for i in range(n):
        m += (pulp.lpDot(A[i], X) >= B[i])
    m.solve()

    result = [pulp.value(var) for var in X]
    result = [1 if i >= 1 / max_f else 0 for i in result]
    result_set = [Sub_Set[i] for i in range(len(Sub_Set)) if result[i] == 1]
    print(result_set)

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
        t = Run_LP(All_Set, Sub_Set)
        time_cost.append(t)
    plt.plot(tests, time_cost)
    plt.show()


if __name__ == '__main__':
    main()
