a = {"satu", 1, "dua", True, 4, 5}  # unorder, not duplicate, unchangable,
print(a)

for i in a:
    print(i)

print("dua" in a)
a.add("add")
print(a)

b = {"update set"}
c = ["update but with list"]
a.update(b)
print(a)

a.update(c)
print(a)
