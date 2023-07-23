d = {'a':2, 'b':3}
c = d['g'] if 'g' in d else 0
print(type(c))# <class 'int'>
print(c) # 0
a = {'g':5}
d.update(a)
print(d) # {'a': 2, 'b': 3, 'g': 5}
print(d.get('abdc', 'aaaa')) #aaaa

sequence = ['a', 'b', 'c']
value = 1

new_dict = dict.fromkeys(sequence, value)

print(new_dict)  # Выведет: {'a': 1, 'b': 1, 'c': 1}
for k in sorted(new_dict):
    print((k))
print(sorted(new_dict))# ['a', 'b', 'c']
