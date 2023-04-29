print(3*"=", "Membaca file external", 3*"=")

file = open("data.txt", mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")
# print(f"baca baris pertama : {file.readline()}")
# print(f"baca baris selanjutnya : {file.readline()}")
print(f"baca file : {file.readlines()}")

print(file.read())

print(f"is the file is closed? {file.closed}")

file.close()
print(f"is the file is closed? {file.closed}")

print("\n================\nMembaca file dengan with\n")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"is the file is closed? {file.closed}")


print(f"is the file is closed? {file.closed}")
