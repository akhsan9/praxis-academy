# ***Hari 2: Dasar-dasar Pemrograman Python (2)***

## 1. Struktur data di Python

### Macam-macam list

* Tentang list

  Tipe data daftar memiliki beberapa metode objek daftar:
```
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
```
* Daftar sebagai Antrian
```
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry sampai
queue.append("Graham")          # Graham sampai
queue.popleft()                 # Yang pertama sampai sekarang pergi

queue.popleft()                 # Yang kedua sampai sekarang pergi

queue                           # Sisa antrian dalam urutan kedatangan
```

* list/daftar tumpukan:
```
list.append -menambahkan item ke akhir daftar., 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print (stack)
```
* List Pemahaman
```
squares = []
for x in range(10):
    print(squares.append(x**2))


listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:

print (
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs)
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

* Jika ekspresi adalah tupel (misalnya dalam contoh sebelumnya), itu harus diberi tanda kurung.(x, y)

vec = [-4, -2, 0, 2, 4]
# buat list baru dengan value dua kali lipat
[x*2 for x in vec]

# filter list untuk mengecualikan angka negatif
[x for x in vec if x >= 0]

# menerapkan function ke semua elemen
[abs(x) for x in vec]

# panggil metode pada setiap elemen
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# buat daftar 2-tupel seperti (number,square)
[(x, x**2) for x in range(6)]

# tupel harus diberi tanda kurung, jika tidak kesalahan akan muncul
[x, x**2 for x in range(6)]

# ratakan daftar menggunakan listcomp dengan dua 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# Daftar dapat berisi ekspresi kompleks dan fungsi bertingkat:
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```

* List bersarang
```
# matriks 3x4 berikut yang diimplementasikan sebagai list 3 list panjang 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# list berikut akan mengubah urutan baris dan kolom:
print(
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
)
hasil
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# The zip()fungsi akan melakukan pekerjaan yang besar untuk kasus penggunaan ini:
print (list(zip(*matrix)))
hasil
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


```

* del/untuk menghapus item: 
```
# untuk mendelete urutan ke-0
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
hasil
[1, 66.25, 333, 333, 1234.5]

# untuk mendelete urutan antara ke 2 sampai 4
del a[2:4]
print(a)
hasil
[1, 66.25, 1234.5]

#tidak ada masukan baris
del a[:]
print(a)
hasil
[]

#del juga dapat digunakan untuk menghapus seluruh variabel:
del a
```
* Tuple dan Urutan

Tupel terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:
```
t = 12345, 54321, 'hello!'
print(t[0])
12345
print(t)
(12345, 54321, 'halo!')

# # Tuple dapat disarangkan:
u = t, (1, 2, 3, 4, 5)
u
u = t, (1, 2, 3, 4, 5)
((12345, 54321, 'halo!'), (1, 2, 3, 4, 5))

# # Tuple tidak dapat diubah:
print(t[0] = 88888)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# Tetapi tuple dapat berisi objek yang bisa berubah:
v = ([1, 2, 3], [3, 2, 1])
print(t)
([1, 2, 3], [3, 2, 1])

```

* Set

 Satu set adalah koleksi tidak berurutan tanpa elemen duplikat. Set objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

 ```
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # menunjukkan bahwa duplikat telah dihapus
{'orange', 'banana', 'pear', 'apple'}

'orange' in basket                 # menguji keanggotaan cepat
True

'crabgrass' in basket
False

# Peragakan operasi set pada huruf unik dari dua kata

a = set('abracadabra')
b = set('alacazam')
a                                  # huruf unik di a
{'a', 'r', 'b', 'c', 'd'}

a - b                              # huruf di a tapi tidak di b
{'r', 'd', 'b'}

a | b                              # huruf a atau b atau keduanya
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

a & b                              # huruf a dan b
{'a', 'c'}

a ^ b                              # huruf dalam a atau b tapi tidak keduanya
{'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'praxis-academy' if x not in 'abc-'}
print(a)
{'d', 's', 'r', 'p', 'y', 'm', 'x', 'e', 'i'}

```
* Dictionaries

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. 

```
tel = {'jack': 4098, 'slamet': 4139}
tel['guido'] = 4127
print(tel)
{'jack': 4098, 'slamet': 4139, 'guido': 4127}

print(tel['jack'])
4098

del tel['slamet']
tel['irvan'] = 4127
print(tel)
{'jack': 4098, 'guido': 4127, 'irvan': 4127}

print(list(tel))
['jack', 'guido', 'irvan']

print(sorted(tel))
['guido', 'irvan', 'jack']

print('slamet' in tel)
False
print('zaky' not in tel)
True

* dict()konstruktor membangun kamus langsung dari urutan pasangan kunci-nilai:

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

* membuat kamus dari ekspresi kunci dan nilai yang berubah-ubah:
{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

* akan lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci jika kuncinya adalah string sederhana:
dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

```

* Teknik Looping
```
* Saat mengulang kamus, kunci dan nilai terkait dapat diambil pada saat yang sama menggunakan items() metode.

kartun = {'naruto': 'the shippuden', 'batman': 'and robin'}
for k, v in kartun.items():
    print(k, v)
naruto the shippuden
batman and robin
* Saat melakukan perulangan melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan enumerate()fungsi.

for i, v in enumerate(['nol', 'setunggal', 'kalih']):
    print(i, v)
0 nol
1 setunggal
2 kalih

* Untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip()fungsi tersebut.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a)
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

* Untuk mengulang urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian panggil reversed()fungsinya.

for i in reversed(range(1, 10, 2)):
    print(i)
9
7
5
3
1

* Untuk mengulang urutan dalam urutan terurut, gunakan sorted()fungsi yang mengembalikan daftar terurut baru sambil membiarkan sumber tidak berubah.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
apple
apple
banana
orange
orange
pear

* Menggunakan set()secara berurutan menghilangkan elemen duplikat. Penggunaan sorted()kombinasi dengan set()lebih dari satu urutan adalah cara idiomatik untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
apple
banana
orange
pear

* lebih sederhana dan lebih aman untuk membuat daftar baru tidak pada saat looping.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
[56.2, 51.7, 55.3, 52.5, 47.8]
```

* More di Conditions
Kondisi yang digunakan dalam pernyataan whiledan ifdapat berisi operator apa pun, tidak hanya perbandingan.
```
string1, string2, string3 = '', 'Tron dheim', 'Hammerance'
non_null = string1 or string2 or string3
print(non_null)
Tron dheim
```

* Membandingkan Urutan"squences" dan Jenis Lain

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan tipe urutan yang sama. Perbandingannya menggunakan leksikografismemesan: pertama, dua item pertama dibandingkan, dan jika berbeda, hal ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, hingga salah satu urutan habis.
```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
    
## 2. *Modules* di Python

* Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran yang .pyditambahkan. Di dalam modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name __. Misalnya, gunakan editor teks favorit Anda untuk membuat file yang disebut fibo.pydi direktori saat ini dengan konten berikut:
```
# Fibonacci numbers module

def fib(n):    # tulis deret Fibonacci hingga n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # kembalikan deret Fibonacci ke n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#lalu di print di file selain fibo.py
import fibo
print(fibo.fib(1000))

print(fibo.fib2(100))

print(fibo.__name__)

hasilnya
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
None
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo

#Jika ingin sering menggunakan suatu fungsi, Anda dapat menetapkannya ke nama lokal:

fib = fibo.fib
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

* Tentang Modul

Sebuah modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi.
```
# Ada varian importpernyataan yang mengimpor nama dari modul langsung ke tabel simbol modul pengimporan. 

from fibo import fib, fib2
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:

from fibo import *
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

#Jika nama modul diikuti oleh as, maka nama berikut asterikat langsung ke modul yang diimpor.

import fibo as fib
fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Ini juga dapat digunakan saat menggunakan fromdengan efek serupa:

from fibo import fib as fibonacci
fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
``` 


## 3. Input Output di Python

* formatan Output Lebih Menarik 

```
year = 2020
event = 'Pilkada serentak'
print(f'Results of the {year} {event}')

* str.format()Metode string membutuhkan usaha lebih manual. Anda masih akan menggunakan {dan }untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan mendetail, tetapi Anda juga perlu memberikan informasi yang akan diformat.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'

* String Literal Terforma

Literal string yang diformat (juga disebut f-string singkatnya) memungkinkan Anda memasukkan nilai ekspresi Python di dalam string dengan mengawali string denganfatauFdan menulis ekspresi sebagai {expression}.
Membulatkan pi ke tiga tempat setelah desimal:

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

Meneruskan bilangan bulat setelah ':'akan menyebabkan bidang itu menjadi jumlah karakter minimum. Ini berguna untuk membuat kolom berbaris.


>>>

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

* Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. '!a'terapkan ascii(), '!s'terapkan str(), dan '!r' terapkan repr():

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

* Metode format String ()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

* Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke str.format()metode.

print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

* Jika argumen kata kunci digunakan dalam str.format()metode ini, nilainya dirujuk dengan menggunakan nama argumen.

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.

* Argumen posisi dan kata kunci dapat digabungkan secara acak:

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.

*  Ini dapat dilakukan hanya dengan meneruskan dict dan menggunakan tanda kurung siku '[]'untuk mengakses kunci.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

* Ini juga dapat dilakukan dengan melewatkan tabel sebagai argumen kata kunci dengan notasi '**'.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

* baris berikut menghasilkan kumpulan kolom yang tersusun rapi yang menghasilkan bilangan bulat serta kotak dan kubusnya:
for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

* Pemformatan String Manual

```
for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # Catat penggunaan 'end' pada li sebelumnya
     print(repr(x*x*x).rjust(4))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

* Ada metode lain str.zfill(), yang mengisi string numerik di sebelah kiri dengan nol. Ini memahami tentang tanda plus dan minus:

'12'.zfill(5)
'00012'

'-3.14'.zfill(7)
'-003.14'

'3.14159265359'.zfill(5)
'3.14159265359'
```

* Pemformatan string lam
```
* Operator% (modulo) juga dapat digunakan untuk pemformatan string. 
contoh:'string' % values%stringvalues

import math
print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.

* Membaca dan Menulis File

open()mengembalikan file objek , dan ini paling sering digunakan dengan dua argumen: .open(filename, mode)

f = open('workfile', 'w')

* Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara penggunaan file tersebut.

Ini adalah praktik yang baik untuk menggunakan withkata kunci saat menangani objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika pengecualian dimunculkan di beberapa titik.

with open('workfile') as f:
     read_data = f.read()

# Ini dapat memeriksa bahwa file telah ditutup secara otomatis.
f.closed
True

Setelah objek file ditutup, baik dengan withpernyataan atau dengan memanggil f.close(), upaya untuk menggunakan objek file secara otomatis akan error.

f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

* Metode Objek File
Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). 
Jika akhir file telah tercapai, f.read()akan mengembalikan string kosong ( '').

f.read()
'This is the entire file.\n'
f.read()
''

* jika f.readline()mengembalikan string kosong, akhir file telah tercapai, sementara baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.
 f.readline()
'This is the first line of the file.\n'
 f.readline()
'Second line of the file\n'
 f.readline()
''

Untuk membaca baris dari file, Anda dapat melakukan loop di atas objek file. Ini hemat memori, cepat, dan mengarah ke kode sederhana:
for line in f:
     print(line, end='')

This is the first line of the file.
Second line of the file

* f.write(string)menulis konten string ke file, mengembalikan jumlah karakter yang ditulis.
f.write('This is a test\n')
15

* Jenis objek lain perlu dikonversi - baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) - sebelum menulisnya:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
18

```

* Menyimpan data terstruktur dengan json
```
Daripada membuat user terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan Anda menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation) .

Jika Anda memiliki sebuah objek x, Anda dapat melihat representasi string JSON-nya dengan baris kode sederhana:

import json
 json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

* Varian lain dari dumps()fungsi tersebut, disebut dump(), hanya membuat serialisasi objek menjadi file teks . Jadi jika fadalah file teks objek dibuka untuk menulis, kita bisa melakukan ini:

json.dump(x, f)

* Untuk memecahkan kode objek lagi, jika fmerupakan objek file teks yang telah dibuka untuk dibaca:

x = json.load(f)




```


## 4. Penanganan *errors dan exceptions*.

Sampai saat ini pesan kesalahan belum lebih dari disebutkan, tetapi jika Anda telah mencoba contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaks dan pengecualian .

```
* kesalahan syntax


while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
    hasil
    SyntaxError: invalid syntax



* Pengecualian

10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

* Penanganan Pengecualian
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih.

while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")

* Klausa pengecualian dapat memberi nama beberapa pengecualian sebagai tupel yang diberi tanda kurung, misalnya:
except (RuntimeError, TypeError, NameError):
     pass

* Sebuah kelas dalam exceptklausa kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasarnya (tetapi tidak sebaliknya - klausa kecuali yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


* Klausa pengecualian terakhir dapat menghilangkan nama pengecualian, untuk berfungsi sebagai karakter pengganti.
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

* The try... exceptPernyataan memiliki opsional lain klausul , yang, ketika hadir, harus mengikuti semua kecuali klausa. Berguna untuk kode yang harus dijalankan jika klausa try tidak memunculkan eksepsi. Sebagai contoh:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

* Klausa pengecualian dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke contoh pengecualian dengan argumen yang disimpan di instance.args. Untuk kenyamanan, contoh pengecualian menentukan __str__()sehingga argumen dapat dicetak secara langsung tanpa harus merujuk .args. 

try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

* Penangan pengecualian tidak hanya menangani pengecualian jika pengecualian tersebut terjadi langsung di klausa coba, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa coba. Sebagai contoh:

def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

* Meningkatkan Pengecualian
```
The raisepernyataan memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Sebagai contoh:

raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere

Jika kelas pengecualian diteruskan, itu akan secara implisit dibuat dengan memanggil konstruktornya tanpa argumen:

raise ValueError  # shorthand for 'raise ValueError()'

Jika Anda perlu menentukan apakah pengecualian dimunculkan tetapi tidak bermaksud menanganinya, bentuk raisepernyataan yang lebih sederhana memungkinkan Anda untuk memunculkan kembali pengecualian:

try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere


```

* Exception Chaining
```
 def func():
...    raise IOError
...
 try:
...     func()
... except IOError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError

Ekspresi yang mengikuti fromharus berupa pengecualian atau None. Rangkaian pengecualian terjadi secara otomatis saat pengecualian dimunculkan di dalam penangan atau finallybagian pengecualian . Rantai pengecualian dapat dinonaktifkan dengan menggunakan idiom:from None

try:

    open('database.sqlite')

except IOError:

    raise RuntimeError from None


Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError


```
* Pengecualian Pengguna
```
* Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk lebih lanjut tentang kelas Python). Pengecualian biasanya harus diturunkan dari Exceptionkelas, baik secara langsung maupun tidak langsung.

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        ```


```
Sumber :
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/tutorial/inputoutput.html
https://docs.python.org/3/tutorial/errors.html



