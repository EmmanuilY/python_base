z = set('asd')
print(z)
z.update([i for i in range(10)])
print(z) # {0, 1, 2, 3, 4, 5, 6, 7, 'a', 's', 8, 9, 'd'}
a = set()
a.update([i for i in range(5)])
print(z-a) # {5, 6, 7, 8, 's', 9, 'a', 'd'}
print(z | a) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 's', 'd'}
print(z & a) #{0, 1, 2, 3, 4}
print(z ^ a) #{5, 6, 7, 8, 9, 'a', 's', 'd'}
print(a > z, z>a) # False True
a.add(range(10))
a.add(['a', 'b']) # TypeError: unhashable type: 'list'
