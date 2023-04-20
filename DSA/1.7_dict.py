a = {
    1: "satu",
    "dua": 2,
    3: "tiga",
    "empat": 4,
}

print(a)
print(type(a))
print("=======")
x = a.get(1)
print(x)
print(a["dua"])
print(a.keys())  # get the dict key
print(a.values())  # get the dict values
a[5] = "lima"  # add new key value
print(a)

# make a list from dict value
listA = list(a.values())
print("list from dict\n", listA)
print(a.items())

if 1 in a.values():
    print("YES")
else:
    print("NO")

del a[5]
# a.pop(5)
# a.popitem() --> last item inserted
# a.clear() delete the dict
print(a)

print("\nloop the dict\n")
for x in a:
    print("key:", x, "val:", a[x])

print("========")
for x in a.keys():
    print(x)
print("========")

for x in a.values():
    print(x)
print("========")

for x in a.items():
    print(x)
print("========")

for x, y in enumerate(a):
    print(x, y)
