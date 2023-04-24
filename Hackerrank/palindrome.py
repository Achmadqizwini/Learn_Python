

def pal(a: str) -> str:
    for i in range(len(a)):
        if a[i] != a[len(a)-i-1]:
            return "not a palindrome"

    return "palindrome"


a = "katak"
res = pal(a)
print(res)
