a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {7, 8, 9, 10, 11, 12}
print(a, "\n", b)
print("\n===========")

a.add(9)
print("add 9\n", a)

x = a.difference(b)
print("a not in b\n", x)

a.difference_update(b)
print("update a that not occure in b\n", a)
a = {1, 2, 3, 4, 5, 6, 7, 8}

a.discard(6)
print("discard value 6\n", a)

x = a.intersection(b)
print("the value that occured in a and b\n", x)

a.intersection_update(b)
print("update set a that have same value with b\n", a)
a = {1, 2, 3, 4, 5, 6, 7, 8}

x = a.isdisjoint(b)
print("is there no items in set a that present in set b?\n", x)

x = a.issubset(b)
print("is all items in a occure in set b?\n", x)

x = a.issuperset(b)
print("is all items in set b occure in set a?\n", x)

a.pop()
print("remove random item from a\n", a)

a.remove(2)
print("remove the items 2\n", a)

x = a.symmetric_difference(b)
print("all items without items that present in both sets\n", x)

a.symmetric_difference_update(b)
print("update variable without items that present in both sets\n", a)

a = {1, 2}
b = {3, 4}

x = a.union(b)
a.update(b)

print("mmerge two sets", x, a)
