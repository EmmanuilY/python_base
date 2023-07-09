d = {'a':2, 'b':3}
c = d['g'] if 'g' in d else 0
print(type(c))# <class 'int'>
print(c) # 0