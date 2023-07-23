pepe = ['a', 2, [1,2]]
pepe_reverse = pepe.reverse()
print(pepe) #[[1, 2], 2, 'a']
print(pepe_reverse) # None
M = [[1,2,3], [4,5,6], [7,8,9]]
New_M = list(map(sum, M))
print(New_M) # [6, 15, 24]
print(list(zip(pepe,New_M))) # [([1, 2], 6), (2, 15), ('a', 24)]
print(dict(zip(New_M,pepe))) # {6: [1, 2], 15: 2, 24: 'a'}

a = ['a', 'b', 'c']
a[:2] = ['g', 'g']
print(a) # ['g', 'g', 'c']
