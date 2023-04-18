a = 3
b = 5

c = a + b
d = a * b
e = a ** b
f = b % a
g = b / a
h = b // a
i = round(g, 2)

print("a:", a, "b:", b)
print(c, "\n", d, e, f, g, h, i)


# bitwise

a1 = 9
b1 = 5

# bitwise OR |
c1 = a1 | b1

print("binary a1: ", format(a1, '08b'))
print("binary b1: ", format(b1, '08b'))
print("--------------------|")
print("binary c1: ", format(c1, '08b'))

# bitwise AND &
print("==========================")
d1 = a1 & b1
print("binary a1: ", format(a1, '08b'))
print("binary b1: ", format(b1, '08b'))
print("--------------------&")
print("binary d1: ", format(d1, '08b'))

# bitwise XOR ^
print("==========================")
e1 = a1 ^ b1
print("binary a1: ", format(a1, '08b'))
print("binary b1: ", format(b1, '08b'))
print("--------------------^")
print("binary e1: ", format(e1, '08b'))
