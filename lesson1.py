#встроенные функции
#abs(-2)
#pow(3, 2)
#print()
#input()
#len()
#list()
#s = {"k": 2}
#p = list(s.values())
#print(p)

#tuple()
#int()
#str()
#dir()

#map(), filter(), return()
#def add(x):
#    return x * 7
#lists = [3, 5, 8, 12]
#add_to = list(map(add, lists))
#print(add_to)

#lists = [3, -5, 8, -12]
#lists = [-3, 5, -8, 2]
#def fact(a):
#   if a < 0:
#    a = abs(a)
#    x = 1
#    for i in range(1, a+1):
#        x *= i
#    return abs(x)
#list_new = list(map(fact, lists))
#print(list_new)

#filter()
#def test(number):
#    if number <=3:
#        return number
#numbers = [1, 19, 13, 3,]
#result = filter(test, numbers)
#print(list(result))

#polindrom = ['анна', 'civic', 'китнаморенерамантик', 'almaz', 'ulukbek']
#for i in polindrom:
#    if i == polindrom:
#        print(i)
#for i in polindrom:
#    if i == i[::1]:
#      print(i, 'polindrom')

#polindrom = ['анна', 'civic', 'китнаморенерамантик', 'almaz', 'ulukbek']
#def is_polindrom(strin):
#    new_str = strin[::-1]
#    if strin.lower() == new_str.lower():
#        return strin
#new_polindrom = list(filter(is_polindrom, polindrom))
#print(new_polindrom)


from functools import reduce

#def proiz(a, b):
#    return a * b
#numbers = [4, 2, 2, 3]
#num = reduce(proiz, numbers)
#print(num)

#lists = list(range(1, 101))
#def app(x):
#    return x**2
#app_to = list(map(app, lists))
#print(app_to)

#def add7(x):
#    print(x+7)
#add7(4)

def add(x, y):
    return x + y