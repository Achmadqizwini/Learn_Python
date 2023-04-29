print("1. write file ")

with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("jonathan jotaroooooo\n")

with open("data2.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")

print("\n2. write file using append\n")

with open("data2.txt", mode="a", encoding="utf-8") as file:
    file.write("dio brando\n")
with open("data2.txt", mode="r") as file:
    content = file.readlines()
    print(content, end="")

print("\n3. write file using r+")

with open("data2.txt", mode="r+", encoding="utf-8") as file:
    file.write("timpa")

with open("data2.txt", mode="r+", encoding="utf-8") as file:
    res = file.read()
    print(res)

print("metode r+ akan menimpa sepanjang panjang teks")
