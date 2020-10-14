# ***Hari 3: OOP dan Pustaka Standar*** #
1. OOP Object Oriented Programming

Pemrograman berorientasi objek ( OOP ) adalah paradigma pemrograman yang didasarkan pada konsep " objek ", jadi didalam bungkus obyek terdapat data dan kode.
* data ini adalah data dalam bentuk field yang biasa disebut atribut/properti. misalnya: property dari laptop bisa berupa merk, warna, jenis processor, ukuran layar, dan lain-lain.
* kode ini adalah dalam bentuk prosedur yang biasa disebut method). misalnya: aksi dari laptop bisa shutdown, restart, sleep, logout, switchuser.
```
Saya membayangkan objek seperti sel biologis dan / atau komputer individu di jaringan, hanya dapat berkomunikasi dengan pesan (jadi pesan datang di awal - butuh beberapa saat untuk melihat bagaimana melakukan pengiriman pesan dalam bahasa pemrograman cukup efisien untuk menjadi berguna).

Alan Kay, 
```

manfaat menggunakan OOP dengan membuat abstraksi dari implementasi. VB.NET dan C # mendukung pewarisan lintas bahasa, memungkinkan kelas yang ditentukan dalam satu bahasa ke kelas subkelas yang ditentukan dalam bahasa lain. 

https://en.wikipedia.org/wiki/Object-oriented_programming
https://en.wikipedia.org/wiki/Class-responsibility-collaboration_card
http://agilemodeling.com/artifacts/crcModel.htm


* Class

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



