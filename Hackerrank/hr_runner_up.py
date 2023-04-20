if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(arr)
    ar = list(arr)
    max_val = max(ar)
    y = -9999999999999
    for i in range(0, n):
        if ar[i] < max_val and ar[i] > y:
            y = ar[i]

    print(y)
