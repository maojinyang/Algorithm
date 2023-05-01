import random

random.seed(42)
sub_set_num = 2


def Init_Set():
    All_Set = ["A", "B", "C", "D", "E", "F", "G", "H"]
    Sub_Set = [["A", "B", "C"],
               ["E", "A", "H"],
               ["D", "C", "G"],
               ["B", "C"],
               ["F", "G"]]
    return All_Set, Sub_Set


def Build_Sub_Set(Pre_All_Set, All_Set):
    if len(list(set(All_Set) - set(Pre_All_Set))) <= sub_set_num:
        return list(set(All_Set) - set(Pre_All_Set))
    num = random.randint(1, sub_set_num)
    sub_num_1 = random.randint(1, num)
    Set_1 = random.sample(list(set(All_Set) - set(Pre_All_Set)), sub_num_1)
    sub_num_2 = num - sub_num_1
    Set_2 = random.sample(Pre_All_Set, sub_num_2)
    return Set_1 + Set_2


def Build_Input(num):
    All_Set = set()
    while len(All_Set) < num:
        item = random.randint(1, 10000)
        All_Set.add(item)

    All_Set = list(All_Set)
    Sub_Set_0 = random.sample(All_Set, sub_set_num)

    Pre_All_Set = Sub_Set_0[:]
    Result = [Sub_Set_0]
    while True:
        Sub_Set_i = Build_Sub_Set(Pre_All_Set, All_Set)
        if len(Sub_Set_i) > 0:
            Pre_All_Set.extend(Sub_Set_i)
            Result.append(Sub_Set_i)
        else:
            break
    # print(Result)
    return All_Set, Result


if __name__ == '__main__':
    Build_Input(5000)
