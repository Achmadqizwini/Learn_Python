a = ("apel", "pisang", "mangga", "semangka")
b = list(a)
b[1] = "jeruk"
a = tuple(b)
print(a)
c = ("melon",)  # note: must add a coma in the end,
a += c
d = a*2
print(d)
print(a)

print("\nunpacking tuples")

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
(green, yellow, *red) = a
print(green)
print(yellow)
print(red)

(green, *yellow, red) = a
print(green)
print(yellow)
print(red)


# tuple methods
print("\ntuple methods\n===========")
print(a)
d = ("apel",)
a += d

print("apel occured", a.count("apel"), "times")

print("index of melon is", a.index("melon"))
