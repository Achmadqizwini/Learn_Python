a = [1, 2, 3, 4, 5]

a.append(10)
print("append 10", a)

b = a.copy()
print(b)

a.extend(b)
print("extend with b", a)

print("there is ", a.count(2), "occurance of 2")

# return the first index of the spesific element
print("the index of value 1 is", a.index(1))

a.insert(0, 100)
print("add 100 in index zero", a)

a.pop(0)
print("pop the index 0", a)

a.remove(1)
print("remove the value 1", a)

a.reverse()
print("reversed:", a)

a.sort()
print("sort ascending", a)

a.sort(reverse=True)
print("sort descending", a)


# A function that returns the length of the value:


def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)

# A function that returns the 'year' value:


def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
cars.sort(reverse=True, key=myFunc)
print(cars)
