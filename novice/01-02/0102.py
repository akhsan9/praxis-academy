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
print("Square root dari 16 yaitu", sqrt(16))

if __name__ == '__main__':
    print('Program ini dijalankan dengan sendirinya')
else:
    print ('program ini sedang diimpor dari modul lain')

 
>>> import sys

# get names of attributes in sys module