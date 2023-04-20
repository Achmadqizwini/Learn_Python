a = "abcdefgh"
print(a)
b = "aaa\nasd"
print(b)
c = r"aa\nss"
print(c, "// use 'r' to ignore \ as a spesial characrer")

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

d = 3*"tu"+"ru"
print(d)

print(a[0])
print(a[2:])
print(a[:3])
print(a[1:5])
print(a[-2:])
print(a[-5:-2])

print("A" + a[1:] + " change first chara")
