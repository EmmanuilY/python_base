a = True
b = 'privet'
c = a if not a else b
print(c)
A = ['a','b'][True]
print(A)
A = ['a','b'][False]
print(A)
number = 0
while number < 10 :
    number += 1
    if number == 11:
        break
else:                       # выполняется после окончания, если не было break и если while  вообще не юзалась
   print('не было прервания')
print(number)