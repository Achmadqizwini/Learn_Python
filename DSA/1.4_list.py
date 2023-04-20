a = [1, 2, 3, 4, 5, 10]
a[5] = 6

print(a[0])  # 1
print(a[2:])  # [3,4,5,6]
print(a[1:5])  # [2,3,4,5]
print(a[-5:-3])  # [2,3]
print(a + [7, 8, 9])  # [1,2,3,4,5,6,7,8,9]

a.append(10)
print(a)  # [1,2,3,4,5,6,7,8,9,10]

a[6:] = []
print(a)

x = [11, 22, 33]
xx = [a, x]
print(xx)  # [[1,2,3,4,5,6],[11,22,33]]

if 1 in a:
    print("true")

# loop
print("== == == == == == == ==\n")

for val in a:
    print(val)

for i in range(len(a)//2):
    print("index", i, "val", a[i])

i = 0
while i < len(a):
    print(a[i])
    i += 1

# short declaration
print("\nshort declaration")
[print(x) for x in a]


# list comprehension
print("==========\nlist comprehension")

b = []
for x in a:
    if x == 1:
        b.append(x)
print(b)

b = [x for x in a if x % 2 == 0]
print(b)
b = [x if x != 2 else 10 for x in a]
print(b)
