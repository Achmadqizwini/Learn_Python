from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
    res = 0
    for i in operations:
        if "--" in i:
            res -= 1
        else:
            res += 1
    return res


arr = ["--X", "X++", "X++"]
result = finalValueAfterOperations(arr)
print(result)


def finalValueAfterOperations(self, operations: List[str]) -> int:
    res = 0
    for i in operations:
        if i[1] == "-":
            res -= 1
        else:
            res += 1
    return res


def finalValueAfterOperations(self, operations: List[str]) -> int:
    return sum(('+' in s) - ('-' in s) for s in operations)


def finalValueAfterOperations(self, operations: List[str]) -> int:
    return sum('+' in s or -1 for s in operations)
