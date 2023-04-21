from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i, j in zip(nums[:n], nums[n:]):
        print(i, j)
        res += [i, j]
    return res


# Example usage
nums = [1, 2, 3, 4, 5, 6]
n = 3
shuffled_nums = shuffle(nums, n)
print(shuffled_nums)

print("== == == === ")


class Solution:
    @staticmethod
    def shuffle2(nums: List[int], n: int) -> List[int]:
        print(list(zip(nums[:n], nums[n:])))
        return [num for t in zip(nums[:n], nums[n:]) for num in t]


# Example usage
nums = [1, 2, 3, 4, 5, 6]
n = 3
shuffled_nums = Solution.shuffle2(nums, n)
print(shuffled_nums)
