word = 'banana'
#word[0] = 'p' #вызовет ошибку, потому что строка неизменяемая
word += 'tree' #строится новая строка и объект ссылается на нее, реализуется через магический метод __add__
reverse = word[::-1] #переворачивание строки