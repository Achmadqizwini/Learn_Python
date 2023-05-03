import ctypes

a = 1200
print(a)
print(id(a))
print(f'\nmemory address where value of a is assigned {hex(id(a))}')

b = a
print(f'memory address where value of b is assigned {hex(id(b))}')

a = 0


def ref_count(address):
    return ctypes.c_long.from_address(address).value


num = [1, 2, 3]
numl = id(num)
print(ref_count(numl))
numk = num
print(ref_count(numl))
