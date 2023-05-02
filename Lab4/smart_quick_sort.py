import sys
import time
from utils import *

sys.setrecursionlimit(1000000)


def smart_partition(nums, left, right):
    """
    * p指向序列左边等于pivot元素的位置
    * q指向序列右边等于Pivot元素的位置
    * i指向从左向右扫面时的元素
    * j指向从右向左扫描时的元素
    return 【比pivot小的元素】【与pivot相等的元素】【比pivot大的元素】
    """
    pivot = nums[left]  # 初始化一个待比较数据
    i = p = left
    j = q = right
    while i < j:
        while i < j and nums[j] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
            if nums[j] == pivot:  # 把相等的数跟q交换位置
                nums[j], nums[q] = nums[q], nums[j]
                q -= 1
            j -= 1
        nums[i] = nums[j]  # 将更小的数放入左边
        while i < j and nums[i] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
            if nums[i] == pivot:  # 把相等的数跟p交换位置
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1
        nums[j] = nums[i]  # 将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot  # 待比较数据放入最终位置
    # p指向的是左边相同元素的下一位，回撤一步，，把相同元素放中间
    p -= 1
    i -= 1
    while p >= left:
        nums[i], nums[p] = nums[p], nums[i]
        i -= 1
        p -= 1
    # q指向的是右边相同元素的下一位，回撤一步，把相同元素放中间
    q += 1
    j += 1
    while q <= right:
        nums[j], nums[q] = nums[q], nums[j]
        q += 1
        j += 1
    return i  # 返回待比较数据最终位置


def quicksort(nums, left, right):
    if left < right:
        index = smart_partition(nums, left, right)
        quicksort(nums, left, index - 1)
        quicksort(nums, index + 1, right)


def quicksort_tail(A, p, r):
    while p < r:
        i = smart_partition(A, p, r)
        if i - p < r - i:
            quicksort_tail(A, p, i - 1)
            p = i + 1
        else:
            quicksort_tail(A, i + 1, r)
            r = i - 1


if __name__ == '__main__':
    DATA = Build_Data(42)
    for data in DATA:
        start_time = time.time()
        quicksort(data, 0, len(data) - 1)
        # print(data)
        end_time = time.time()
        print(end_time - start_time)
