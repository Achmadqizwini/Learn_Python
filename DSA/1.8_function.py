def func(fname: str):
    print("hello " + fname)


func("hendri")
func("aqi")


def func2(*fname: str):  # use * args if u dont know how many argument that will be passed to your func
    print(fname[0])


func2("hello", "world")

# recursion

# type hints


def rec(k: int) -> int:
    if k > 0:
        result = k + rec(k-1)
    else:
        result = 0
    return result


print(rec(4))

# default arghument


def say_hello(hello, name, greetings="gpood morning"):
    print(f"{hello} {name}, {greetings}. welcome to the world")


say_hello("hai", "aqiz")


def pow(num1, num2):
    result = num1**num2
    return result


res = pow(2, 3)
print(res)


def pow(num1=5, num2=2):
    result = num1**num2
    return result


print(pow())


# *args

print("\n=====================")
print("ARGS IN FUNCTION \n")


def func(nama, tinggi, berat):
    print(f"{nama} is {tinggi} and {berat}")


func("aqiz", 162, 50)


def func2(data_list):
    data = data_list.copy()

    name = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{name} is {tinggi} and {berat}")


func2(["aqiz", 162, 50])


def argument(*args):
    name = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{name} is {tinggi} and {berat}")


argument("aqiz", 175, 60)


def arg(*args):
    for i in args:
        print(i, end=" ")


arg(1, 2, 3)
arg("makan", "pisang", "ondol")
print("\n")

# kwargs
print("\n=================")
print("KWARGS IN FUNCTION\n")


def kwargg(**kwargs):
    name = kwargs["name"]
    age = kwargs["age"]
    print(f"hallo {name}, are you {age} years old?")


kwargg(name="aqiz", age="120")


def operation(*args, **kwargs):
    res = 0
    if kwargs["option"] == "tambah":
        print("operasi penjumlahan")
        res = sum(args)
    elif kwargs["option"] == "kali":
        print("operasi perkalian")
        res = 1
        for i in args:
            res *= i
    else:
        print("tidak ada operasi")
    print(f"the result is: {res}")


operation(1, 2, 3, 4, 5, option="tambah")
operation(1, 2, 3, 4, 5, option="kali")
