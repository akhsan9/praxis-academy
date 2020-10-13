fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print (fruits.count('apple')) # menghitung berapa kali x muncul dalam daftar.

print (fruits.count('tangerine')) # 

print (fruits.index('banana'))

print (fruits.index('banana', 4))  # mencari kata banana mulai dari posisi 4

print (fruits.reverse())
print (fruits) # untuk membalikkan posisi item dari tempatnya

fruits.append('grape')
print (fruits) # menambahkan item ke akhir daftar

fruits.sort()
print (fruits) # mengurutkan item dari daftar ditempat

print (fruits.pop()) # menghapus item pada posisi tertentu dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop()menghapus dan mengembalikan item terakhir dalam daftar. 

squares = []
for x in range(10):
    print(squares.append(x**2))

print (squares)


print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print ([x*2 for x in vec])

# filter the list to exclude negative numbers
print ([x for x in vec if x >= 0])

# apply a function to all the elements
print ([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print ([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print ([(x, x**2) for x in range(6)])


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print (stack)

stack.pop()

print (stack)

stack.pop()

stack.pop()

print (stack)

#untuk delete urutan ke-0
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)



from collections import deque
queue = deque(["ibran", "adi", "iqlima"])
queue.append("alan")           
queue.append("rino")          
print (queue.popleft()) 
print (queue)

basket = {'apel', 'jeruk', 'apel', 'pear', 'jeruk', 'banana'}
print(basket)                      # untuk menampilkan gandaan yang dihapus

print ('apel' in basket)                 # untuk mempercepat test member

print ('salak' in basket)


from math import sqrt
print("Square root of 16 is", sqrt(16))


year = 9-12-2020
event = 'pilkada'
print(f'Results of the {year} {event}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

import math
print(f'nilai pi matematika {math.pi:.3f}.')

print('mulai labsos di "{}" - {}!'.format('praxis', 'academy'))


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

a = {x for x in 'praxis-academy' if x not in 'abc-'}
print(a)


tel = {'jack': 4098, 'slamet': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['slamet']
tel['irvan'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('slamet' in tel)

print('zaky' not in tel)

kartun = {'naruto': 'the shippuden', 'batman': 'and robin'}
for k, v in kartun.items():
    print(k, v)

for i, v in enumerate(['nol', 'setunggal', 'kalih']):
    print(i, v)

for i in reversed(range(1, 10, 2)):
    print(i)


string1, string2, string3 = '', 'Tron dheim', 'Hammerance'
non_null = string1 or string2 or string3
print(non_null)

import fibo
print(fibo.fib(1000))

print(fibo.fib2(100))

print(fibo.__name__)

year = 2020
event = 'Pilkada serentak'
print(f'Results of the {year} {event}')
    