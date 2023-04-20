a = {"name": "achmad", "age": 12, "address": "disana"}
b = a.copy()
print(a)
print("\n")

c = (1, 2, 3)
d = ("value")

e = dict.fromkeys(c, d)
print(e)
print("get name:", a.get("name"))

print(a.keys())
print(a.values())
print(a.items())

a.pop("age")
print(a)

a.update({"age": 10})
print(a)

a.setdefault("age", 100)
print(a)
