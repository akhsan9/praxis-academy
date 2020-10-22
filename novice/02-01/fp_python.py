#First-Class Functions
def create_logger(message):
   def log():
      print(('Menampilkan pesan: ') + message)
   return log #Return a function
my_logger = create_logger('Hello World')
my_logger()


#Assigning Functions to Variables

def hof_product(multiplier):
    return lambda x: x * multiplier

mult6 = hof_product(6)
print(mult6(6)) # 36



#Passing Functions as Parameters
def formalGreeting ():
   print ("How are you?")

def casualGreeting ():
   print ("What's up?")

def casual(func):
   func()

casual(casualGreeting) 



#Higher-Order Functions
def add2(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers

print(add2([1, 2, 3]))



                              # dengan map

my_list = [1, 2, 3]
                              # Program untuk menghasilkan kuadrat bilangan 
kuadrat = list(map(lambda x: x*2, my_list)) 

                              # Output: [2,4,6] 
print(kuadrat) 



my_list = [1975, 1997, 2002, 1995, 1985]
                              # Program untuk menghasilkan kuadrat bilangan 
kuadrat = list(map(lambda x: 2018-x, my_list)) 

                              # Output: [2,4,6] 
print(kuadrat) 




 # Declare a list for filtering
students = {'Mark': {'age': 18},
             'John': {'age': 27},
             'Jane': {'age': 14},
             'Tony': {'age': 24}}
 


 # Define a function for filtering
def qualify_student(x):
     _, info = x
     condition0 = info['age'] >= 18
     return condition0
 


 # Create a dict of qualified students
qualified_students = dict(filter(qualify_student, students.items()))
print (qualified_students)



#reduce
# Import the needed module
from functools import reduce
 
 # Create a list for reducing
primes = [5, 7, 1, 8, 4]
 
 # Reduce the list
total = reduce(lambda x, y: x + y, primes)
print (total)



#Higher-Order Function
strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']
def mapForEach(arr, fn):
    newArray = []
    for i in range(len(arr)):
        newArray.append(fn(arr[i]))
    return newArray

lenArray = mapForEach(strArray, lambda x: len(x))
print(lenArray)






 