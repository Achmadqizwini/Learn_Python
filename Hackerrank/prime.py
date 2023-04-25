def prime(num: int) -> str:
    for i in range(3, num):
        if num % i == 0:
            return "not a prime"
    return "prime"


print(prime(1))
