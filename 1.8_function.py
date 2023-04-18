def func(fname: str):
    print("hello " + fname)


func("hendri")
func("aqi")


def func2(*fname: str):  # use * args if u dont know how many argument that will be passed to your func
    print(fname[0])


func2("hello", "world")

# recursion


def rec(k: int) -> int:
    if k > 0:
        result = k + rec(k-1)
    else:
        result = 0
    return result


print(rec(4))
