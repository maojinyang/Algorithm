import random


def Build_Data(seed):
    random.seed(seed)
    part_num = 11
    nums = 1000
    ratios = [0.0] + [0.1 * i for i in range(1, part_num)]
    DATA_LIST = []

    for ratio in ratios:
        repeat_item = random.randint(1, 10000)
        data = [repeat_item for _ in range(round(nums * ratio))]
        for _ in range(nums - len(data)):
            data.append(random.randint(1, 10000))
        assert len(data) == nums
        random.shuffle(data)
        DATA_LIST.append(data)
    return DATA_LIST


if __name__ == '__main__':
    Build_Data(42)
