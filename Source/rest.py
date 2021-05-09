a = {'name': '张三', 'age': 100, 'pp': [1, 2, 4]}
b = a.copy()

a['pp'].append(5)

print(id(a)) # 4302864832
print(id(b)) # 4302865024

print(a) # {'name': '张三', 'age': 100, 'pp': [1, 2, 4, 5]}
print(b) # {'name': '张三', 'age': 100, 'pp': [1, 2, 4, 5]}



