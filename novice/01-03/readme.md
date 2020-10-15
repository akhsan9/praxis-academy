# ***Hari 3: OOP dan Pustaka Standar*** #
1. OOP Object Oriented Programming

Pemrograman berorientasi objek ( OOP ) adalah paradigma pemrograman yang didasarkan pada konsep " objek ", jadi didalam bungkus obyek terdapat data dan kode.
* data ini adalah data dalam bentuk field yang biasa disebut atribut/properti. misalnya: property dari laptop bisa berupa merk, warna, jenis processor, ukuran layar, dan lain-lain.
* kode ini adalah dalam bentuk prosedur yang biasa disebut method). misalnya: aksi dari laptop bisa shutdown, restart, sleep, logout, switchuser.
```
Saya membayangkan objek seperti sel biologis dan / atau komputer individu di jaringan,
 hanya dapat berkomunikasi dengan pesan (jadi pesan datang di awal - butuh beberapa saat 
  untuk melihat bagaimana melakukan pengiriman pesan dalam bahasa pemrograman
   cukup efisien untuk menjadi berguna).

Alan Kay, 
```

manfaat menggunakan OOP dengan membuat abstraksi dari implementasi. VB.NET dan C # mendukung pewarisan lintas bahasa, memungkinkan kelas yang ditentukan dalam satu bahasa ke kelas subkelas yang ditentukan dalam bahasa lain. 

https://en.wikipedia.org/wiki/Object-oriented_programming
https://en.wikipedia.org/wiki/Class-responsibility-collaboration_card
http://agilemodeling.com/artifacts/crcModel.htm

2. CRC card

Class-responsibility-collaboration/Kartu kelas-tanggung jawab-kolaborasi ( CRC ) adalah alat curah pendapat(brainstorming) yang digunakan dalam desain perangkat lunak berorientasi objek . Mereka awalnya diusulkan oleh Ward Cunningham dan Kent Beck sebagai alat pengajaran,tetapi juga populer di kalangan desainer ahli dan direkomendasikan oleh pendukung program ekstrim . Martin Fowler telah menggambarkan kartu CRC sebagai alternatif yang layak untuk diagram urutan UML untuk merancang dinamika interaksi dan kolaborasi objek.

Kartu CRC biasanya dibuat dari kartu indeks . Anggota sesi brainstorming akan menulis satu kartu CRC untuk setiap kelas / objek yang relevan dari desain mereka. Kartu tersebut dibagi menjadi tiga area:

* Di atas kartu, Class name/nama kelas, Kata benda harus berubah menjadi kelas kartu
* Di sebelah kiri, responsibiliy/tanggung jawab kelas, kata kerja biasanya berubah menjadi tanggung jawab dari kartu.
* Di sebelah kanan, collaborators/kolaborator (kelas lain) yang berinteraksi dengan kelas ini untuk memenuhi tanggung jawabnya, kolaborator adalah kartu lain dengan kartu yang akan berinteraksi. 



3. Object-Oriented Programming di Python.
* self
Metode kelas hanya memiliki satu perbedaan spesifik dari fungsi biasa - mereka harus memiliki nama depan tambahan yang harus ditambahkan ke awal daftar parameter, tetapi Anda tidak memberikan nilai untuk parameter ini saat Anda memanggil metode, Python akan menyediakan Itu. Variabel khusus ini mengacu pada objek self itu , dan menurut konvensi, itu diberi nama self.

* Class

Template untuk membuat objek yang ditentukan pengguna. Definisi kelas biasanya berisi definisi metode yang beroperasi pada instance kelas.

Kelas yang paling sederhana ditunjukkan pada contoh berikut (simpan sebagai oop_simplestclass.py).
```
class Person:
    pass  # An empty block

p = Person()
print(p)
```
Keluaran:
```
$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>
```
* Metode
Fungsi yang didefinisikan di dalam badan kelas. Jika dipanggil sebagai atribut dari sebuah instance dari kelas itu, metode tersebut akan mendapatkan objek instance tersebut sebagai argumen pertamanya (yang biasanya disebut self). Lihat fungsi dan cakupan bersarang .

kelas / objek dapat memiliki metode seperti fungsi kecuali bahwa kita memiliki selfvariabel tambahan . Sekarang kita akan melihat contoh (simpan sebagai oop_method.py).
```
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
```
Keluaran:
```
$ python oop_method.py
Hello, how are you?
```

* __init__metode

The __init__Metode dijalankan segera sebagai objek dari suatu kelas adalah instantiated (yaitu dibuat). Metode ini berguna untuk melakukan inisialisasi apa pun (yaitu meneruskan nilai awal ke objek Anda) yang ingin Anda lakukan dengan objek Anda. 

Contoh (simpan sebagai oop_init.py):
```
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
```
Keluaran:
```
$ python oop_init.py
Hello, my name is Swaroop
```
* Variabel Kelas Dan Objek 

Variabel kelas dibagi - mereka dapat diakses oleh semua contoh kelas itu. Hanya ada satu salinan variabel kelas dan ketika salah satu objek membuat perubahan ke variabel kelas, perubahan itu akan terlihat oleh semua contoh lainnya.

Variabel objek dimiliki oleh masing-masing objek / instance kelas. Dalam hal ini, setiap objek memiliki salinan bidangnya sendiri, yaitu mereka tidak dibagikan dan tidak terkait dengan cara apa pun ke bidang dengan nama yang sama dalam contoh yang berbeda. Sebuah contoh akan membuat ini mudah untuk dipahami (simpan sebagai oop_objvar.py):

```
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```
Keluaran:
```
$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.
```
* Warisan(Inheritance)
Salah satu manfaat utama dari pemrograman berorientasi objek adalah penggunaan kembali kode dan salah satu cara ini dicapai adalah melalui mekanisme pewarisan . Pewarisan dapat dibayangkan sebagai penerapan hubungan tipe dan subtipe antar kelas.

the SchoolMemberkelas dalam situasi ini dikenal sebagai kelas dasar atau superclass . The Teacherdan Studentkelas disebut kelas turunan atau subclass .

Sekarang kita akan melihat contoh ini sebagai program (simpan sebagai oop_subclass.py):
```
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
```
Keluaran:
```
$ python oop_subclass.py
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"
```
4. Class

Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat kelas baru membuat jenis objek baru, memungkinkan instance baru dari jenis itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk mengubah statusnya.

Template untuk membuat objek yang ditentukan pengguna. Definisi kelas biasanya berisi definisi metode yang beroperasi pada instance kelas.

```

class Robot:
"""Represents a robot, with a name."""

# A class variable, counting the number of robots
population = 0

def __init__(self, name):
"""Initializes the data."""
self.name = name
print("(Initializing {})".format(self.name))

# When this person is created, the robot
# adds to the population
Robot.population += 1

def die(self):
"""I am dying."""
print("{} is being destroyed!".format(self.name))

Robot.population -= 1

if Robot.population == 0:
print("{} was the last one.".format(self.name))
else:
print("There are still {:d} robots working.".format(
Robot.population))

def say_hi(self):
"""Greeting by the robot.

Yeah, they can do that."""
print("Greetings, my masters call me {}.".format(self.name))

@classmethod
def how_many(cls):
"""Prints the current population."""
print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```
Keluaran:
```
$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.
```
* Warisan(Inheritance)

he SchoolMemberkelas dalam situasi ini dikenal sebagai kelas dasar atau superclass . The Teacherdan Studentkelas disebut kelas turunan atau subclass .

Sekarang kita akan melihat contoh ini sebagai program (simpan sebagai oop_subclass.py):
```
class SchoolMember:
'''Represents any school member.'''
def __init__(self, name, age):
self.name = name
self.age = age
print('(Initialized SchoolMember: {})'.format(self.name))

def tell(self):
'''Tell my details.'''
print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
'''Represents a teacher.'''
def __init__(self, name, age, salary):
SchoolMember.__init__(self, name, age)
self.salary = salary
print('(Initialized Teacher: {})'.format(self.name))

def tell(self):
SchoolMember.tell(self)
print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
'''Represents a student.'''
def __init__(self, name, age, marks):
SchoolMember.__init__(self, name, age)
self.marks = marks
print('(Initialized Student: {})'.format(self.name))

def tell(self):
SchoolMember.tell(self)
print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
# Works for both Teachers and Students
member.tell()
```
Keluaran:
```
$ python oop_subclass.py
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"
```
2. Class

* Contoh Cakupan dan Namespaces
Ini adalah contoh yang menunjukkan cara mereferensikan cakupan dan namespace yang berbeda, dan bagaimana globalserta nonlocalmemengaruhi pengikatan variabel:
```
def scope_test():
def do_local():
spam = "local spam"

def do_nonlocal():
nonlocal spam
spam = "nonlocal spam"

def do_global():
global spam
spam = "global spam"

spam = "test spam"
do_local()
print("After local assignment:", spam)
do_nonlocal()
print("After nonlocal assignment:", spam)
do_global()
print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

Output dari kode contoh tersebut adalah:

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

* Pandangan Pertama di Kelas

Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.
```
* Sintaks Definisi Kelas

class ClassName:
<statement-1>
.
.
.
<statement-N>

* Objek Kelas

Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi.

class MyClass:
"""A simple example class"""
i = 12345

def f(self):
return 'hello world'

Instansiasi kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):

x = MyClass()

Operasi instantiation ("memanggil" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan contoh yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu, kelas dapat mendefinisikan metode khusus bernama __init__(), seperti ini:

def __init__(self):
self.data = []

Ketika sebuah kelas mendefinisikan sebuah __init__()metode, instansiasi kelas secara otomatis dipanggil __init__()untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:

x = MyClass()

Tentu saja, __init__()metode tersebut mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan ke operator instantiation kelas diteruskan ke __init__(). Sebagai contoh,
>>>

>>> class Complex:
... def __init__(self, realpart, imagpart):
... self.r = realpart
... self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

```

* Objek Instance

atribut data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C ++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, variabel tersebut muncul saat pertama kali ditetapkan. Misalnya, jika xinstance MyClassdibuat di atas, potongan kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak:
```
x.counter = 1
while x.counter < 10:
x.counter = x.counter * 2
print(x.counter)
del x.counter
```

* Objek Metode

```
Biasanya, metode dipanggil tepat setelah terikat:

x.f()

Dalam MyClasscontoh, ini akan mengembalikan string . Namun, tidak perlu langsung memanggil metode: merupakan objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:'hello world'x.f

xf = x.f
while True:
print(xf())

akan terus mencetak sampai akhir waktu.hello world
```

* Variabel Kelas dan Instans
```
Secara umum, variabel instance untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang digunakan bersama oleh semua instance kelas:

class Dog:

kind = 'canine' # class variable shared by all instances

def __init__(self, name):
self.name = name # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind # shared by all dogs
'canine'
>>> e.kind # shared by all dogs
'canine'
>>> d.name # unique to d
'Fido'
>>> e.name # unique to e
'Buddy'

daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance Dog :

class Dog:

tricks = [] # mistaken use of a class variable

def __init__(self, name):
self.name = name

def add_trick(self, trick):
self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks # unexpectedly shared by all dogs
['roll over', 'play dead']

Desain kelas yang benar harus menggunakan variabel contoh sebagai gantinya:

class Dog:

def __init__(self, name):
self.name = name
self.tricks = [] # creates a new empty list for each dog

def add_trick(self, trick):
self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

```

* Komentar Acak
```
Jika nama atribut yang sama muncul di instance dan di kelas, maka pencarian atribut memprioritaskan instance tersebut:
>>>

>>> class Warehouse:
purpose = 'storage'
region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east

Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas itu. Definisi fungsi tidak perlu disertakan secara tekstual dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga boleh. Sebagai contoh:

# Function defined outside the class
def f1(self, x, y):
return min(x, x+y)

class C:
f = f1

def g(self):
return 'hello world'

h = g

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari self argumen:

class Bag:
def __init__(self):
self.data = []

def add(self, x):
self.data.append(x)

def addtwice(self, x):
self.add(x)
self.add(x)

* Inheritance/Warisan

entu saja, fitur bahasa tidak akan layak disebut "kelas" tanpa mendukung pewarisan. Sintaks untuk definisi kelas turunan terlihat seperti ini:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

Nama BaseClassNameharus ditentukan dalam lingkup yang berisi definisi kelas turunan. Sebagai pengganti nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Ini dapat berguna, misalnya, ketika kelas dasar ditentukan di modul lain:

class DerivedClassName(modname.BaseClassName):

Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:

    - Gunakan isinstance()untuk memeriksa tipe instance: hanya akan jika ada atau beberapa kelas turunan dari .isinstance(obj, int)Trueobj.__class__intint

    - Gunakan issubclass()untuk memeriksa warisan kelas: adalah karena merupakan subkelas dari . Namun, adalah karena tidak subclass dari .issubclass(bool, int)Trueboolintissubclass(float, int)Falsefloatint

* Multiple inhertance(pewarisan ganda)

Python juga mendukung bentuk multiple inheritance. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

* Variabel Pribadi

Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah (mis. _spam) Harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode, atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Name mangling berguna untuk membiarkan subclass mengganti metode tanpa memutus panggilan metode intraclass. Sebagai contoh:

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

* Peluang dan Berakhir/odds and ends

Terkadang berguna untuk memiliki tipe data yang mirip dengan “record” Pascal atau “struct” C, menggabungkan beberapa item data bernama. Definisi kelas kosong akan bekerja dengan baik:

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


* Iterator

Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat diulang menggunakan forpernyataan:

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


    s = 'abc'
    it = iter(s)
     it
<iterator object at 0x00A1DB50>
     next(it)
'a'
     next(it)
'b'
    next(it)
'c'
    next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration

Jika kelas mendefinisikan __next__(), maka __iter__()dapat mengembalikan self:

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



    rev = Reverse('spam')
    iter(rev)
<__main__.Reverse object at 0x00A1DB50>
    for char in rev:
...     print(char)
...
m
a
p
s

* Generator

Generator adalah alat sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakanyieldpernyataan kapan pun mereka ingin mengembalikan data. Setiap kalinext()dipanggil, generator melanjutkan dari tempat yang ditinggalkannya (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dibuat dengan sangat mudah:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]



    for char in reverse('golf'):
...     print(char)
...
f
l
o
g


* Ekspresi Generator

Ekspresi generator lebih kompak tetapi kurang fleksibel dibandingkan definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

Contoh:


    sum(i*i for i in range(10))                 # sum of squares
285

    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

    unique_words = set(word for line in page  for word in line.split())

    valedictorian = max((student.gpa, student.name) for student in graduates)

    data = 'golf'
    list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']


```





