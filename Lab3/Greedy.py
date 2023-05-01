from utils import *


def Run_Greedy(All_Set, Sub_Set):
    select = []
    while len(All_Set) != 0:
        select_item = None
        max_length = -1
        for item in Sub_Set:
            intersection = list(set(item) & set(All_Set))  # 求交集
            print(intersection)
            if len(intersection) > max_length:
                max_length = len(intersection)
                select_item = item
        All_Set = list(set(All_Set) - set(select_item))  # 求差集
        select.append(select_item)
    print(select)


def main():
    All_Set, Sub_Set = Init_Set()
    Run_Greedy(All_Set, Sub_Set)


if __name__ == '__main__':
    main()
