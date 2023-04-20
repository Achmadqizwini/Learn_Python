a = "abcDEfghiJK123abc"

print("capitalized first item\n", a.capitalize())

print("to lower\n", a.casefold())
print("to lower\n", a.lower())

print("centered str\n", a.center(50))
print("count ab\n", a.count("ab"))

print("encode str", a.encode())
print("is the str ends with c?\n", a.endswith("c"))

print("\nfind the index of c\n", a.find("c"))
print("find the index of c\n", a.index("b"), "(with index method)")
print("find the last index of c\n", a.rfind("c"))
print("find the last index of c\n", a.rindex("b"), "(with index method)")

b = "\nthis car only {price: .2f} dollars"
print(b.format(price=53))


print("\n", a, "\nis all the characters ... ")
print("alnum?", a.isalnum())
print("alpha?", a.isalpha())
print("ascii?", a.isascii())
print("decimal?", a.isdecimal())
print("digit?", a.isdigit())
print("is an identifier?", a.isidentifier())
print("lower?", a.islower())
print("numeric?", a.isnumeric())
print("upper?", a.isupper())
print("whitespace?", a.isspace())
print("printable?", a.isprintable())
print("follow the rules of title?", a.istitle())

print("\n")
c = ("1", "2", "c")
print(c, "join with #==> ", "#".join(c))

x = str.maketrans("c", "C")
print("replace c with C\n", a.translate(x))
x = a.replace("C", "c")
print("replace C with c\n", a.translate(x))

d = "i love banana nana nan nanana"
x = d.split(" ")
print(d, "convert to list\n", x)
