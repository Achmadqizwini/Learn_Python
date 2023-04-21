from typing import List


def leftRightDifference(nums: List[int]) -> List[int]:
    res = []
    a = sum(nums)
    leftSum = 0
    for i, j in enumerate(nums):
        leftSum += j
        res.append(abs(leftSum - a))
        a -= j

    return res


num = [10, 4, 8, 3]
a = leftRightDifference(num)
print(a)


a = ["alice and bob love leetcode", "i think so too",
     "this is great thanks very much"]

for word in a:
    b = word.split()
    print(b)
