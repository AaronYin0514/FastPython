import copy

a = (1, 2, 3)

b = copy.copy(a)
c = copy.deepcopy(a)

print(id(a)) # 4413476288
print(id(b)) # 4413476288
print(id(c)) # 4413476288




