from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # print("iii:  ", nums[i], " // ", nums[j])

            if nums[i] == nums[j]:
                count += 1
    return count


a = [1, 2, 3, 1, 1, 3]
res = numIdenticalPairs(a)
print(res)
