print("test")
a = "test 2"

print("LAMBDA FUNC")


def kuadrat(num): return num**2
# kuadrat = lambda num : num**2


print(kuadrat(3))

my_list = [(2, 3), (1, 5), (3, 1)]
print(my_list)

sorrr = sorted(my_list, key=lambda x: x[1])
srr = sorted(my_list)
print(sorrr)
print(srr)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_data = list(filter(lambda x: x < 5, data))
odd = list(filter(lambda x: x % 2 != 0, data))
print(new_data)
print(odd)

print("\n ANONYMOUS FUNCTION")
print("==============")


def pangkat(n):
    return lambda num: num**n


pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(6)}")
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(4)}")
print(f"pangkat 2 = {pangkat(2)(4)}")
