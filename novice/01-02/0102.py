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