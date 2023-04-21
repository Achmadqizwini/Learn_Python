from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        res.append(count)

    return res


a = [8, 1, 2, 2, 3]
b = smallerNumbersThanCurrent(a)
print(b)


def smallerNumbersThanCurrent2(nums: List[int]) -> List[int]:
    temp = sorted(nums)
    mapping = {}
    res = []
    for i in range(len(nums)):
        # print("aa", temp[i], i)
        if temp[i] not in mapping:
            mapping[temp[i]] = i
    for i in nums:
        res.append(mapping[i])
    return res


a = [8, 1, 2, 2, 3]
b = smallerNumbersThanCurrent2(a)
print(b)


def smallerNumbersThanCurrent3(nums: List[int]) -> List[int]:
    temp = sorted(nums)
    dc = {item: temp.index(item) for item in temp}
    return [dc[item] for item in nums]


a = [8, 1, 2, 2, 3]
b = smallerNumbersThanCurrent3(a)
print(b)


def smallerNumbersThanCurrent4(nums: List[int]) -> List[int]:
    temp = sorted(nums)
    mapping = {}
    for item in temp:
        mapping[item] = temp.index(item)
    return [mapping[item] for item in nums]


a = [8, 1, 2, 2, 3]
b = smallerNumbersThanCurrent4(a)
print(b)
