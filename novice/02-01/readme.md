# ***Minggu 02***
## Hari 1: Functional Programming

Pemrograman Fungsional adalah gaya pengkodean yang berfokus pada menentukan apa yang harus dilakukan, daripada melakukan beberapa tindakan. Pemrograman fungsional berasal dari gaya berpikir matematis di mana Anda menentukan jenis input yang masuk ke suatu fungsi dan jenis keluaran yang dapat kita harapkan dari fungsi. Dalam kode fungsional, keluaran dari fungsi hanya bergantung pada argumen yang dilewati. Memanggil fungsi f untuk nilai x yang sama harus mengembalikan hasil yang sama f (x) tidak peduli berapa kali Anda meneruskannya. Jadi, ini membutuhkan gaya berpikir yang sangat berbeda di mana Anda jarang mengubah keadaan.

Pemrograman Fungsional adalah paradigma pemrograman populer yang terkait erat dengan dasar matematika ilmu komputer. Meskipun tidak ada definisi yang tegas tentang apa yang merupakan bahasa fungsional, kami menganggapnya sebagai bahasa yang menggunakan fungsi untuk mengubah data.

### Karakteristik pemrograman fungsional

Bahasa fungsional murni harus mendukung konstruksi berikut:

* Fungsi sebagai objek kelas pertama, yang berarti Anda harus dapat menerapkan semua konstruksi menggunakan data, ke fungsi juga.

Menggunakan fungsi sebagai objek kelas pertama berarti menggunakannya dengan cara yang sama seperti Anda menggunakan data. Jadi, Anda bisa meneruskannya sebagai parameter seperti meneruskan fungsi ke fungsi lain sebagai argumen

* Fungsi murni; seharusnya tidak ada efek samping di dalamnya

Ada berbagai fungsi bawaan dalam Python yang dapat membantu menghindari kode prosedural dalam fungsi.

* Cara dan konstruksi untuk membatasi penggunaan for loop

Loop masuk ke dalam gambar saat Anda ingin mengulang kumpulan objek dan menerapkan beberapa jenis logika atau fungsi.

* Dukungan yang baik untuk rekursi

Rekursi adalah metode pemecahan masalah menjadi submasalah yang pada dasarnya memiliki jenis yang sama dengan masalah aslinya. Anda memecahkan masalah dasar dan kemudian menggabungkan hasilnya. Biasanya ini melibatkan fungsi yang memanggil dirinya sendiri.

### Konsep Pemrograman Fungsional

Bahasa fungsional adalah bahasa deklaratif , mereka memberi tahu komputer hasil apa yang mereka inginkan. Ini biasanya kontras dengan bahasa imperatif yang memberi tahu komputer langkah apa yang harus diambil untuk memecahkan masalah.

Beberapa fitur Python dipengaruhi oleh Haskell , bahasa pemrograman yang murni berfungsi. Untuk mendapatkan pemahaman yang lebih baik tentang apa itu bahasa fungsional, mari kita lihat fitur-fitur di Haskell yang dapat dilihat sebagai ciri fungsional yang diinginkan:

* Fungsi Murni - tidak memiliki efek samping, yaitu tidak mengubah status program. Dengan masukan yang sama, fungsi murni akan selalu menghasilkan keluaran yang sama.


fungsi murni untuk mengalikan angka dengan 2:
```
def multiply_2_pure(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers

original_numbers = [1, 3, 5, 10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers) # [1, 3, 5, 10]
print(changed_numbers)  # [2, 6, 10, 20]
```

* Kekekalan - data tidak dapat diubah setelah dibuat. Ambil contoh membuat Listdengan 3 item dan menyimpannya dalam variabel my_list. Jika my_listtidak dapat diubah, Anda tidak akan dapat mengubah item satu per satu. Anda harus menyetel my_listke baru Listjika Anda ingin menggunakan nilai yang berbeda.

Python menawarkan beberapa tipe data yang tidak dapat diubah, yang populer adalah Tuple. Mari kontraskan Tuple dengan List , yang bisa berubah:
```
mutable_collection = ['Tim', 10, [4, 5]]
immutable_collection = ('Tim', 10, [4, 5])

# Reading from data types are essentially the same:
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5]

# Let's change the 2nd value from 10 to 15
mutable_collection[1] = 15

# This fails with the tuple
immutable_collection[1] = 15
```

* Fungsi Urutan Tinggi - fungsi dapat menerima fungsi lain sebagai parameter dan fungsi dapat mengembalikan fungsi baru sebagai keluaran. Ini memungkinkan kita untuk mengabstraksi tindakan, memberi kita fleksibilitas dalam perilaku kode kita.

Haskell juga memengaruhi iterator dan generator di Python melalui pemuatan lambatnya, tetapi fitur itu tidak diperlukan untuk bahasa fungsional.

Ingatlah bahwa Fungsi Orde Tinggi menerima fungsi sebagai argumen atau mengembalikan fungsi untuk diproses lebih lanjut. Mari kita ilustrasikan betapa sederhananya keduanya dapat dibuat dengan Python.

Pertimbangkan fungsi yang mencetak baris beberapa kali:
```
def write_repeat(message, n):
    for i in range(n):
        print(message)

write_repeat('Hello', 5)
```

### Ekspresi Lambda

Ekspresi lambda adalah fungsi anonim. Saat kami membuat fungsi dengan Python, kami menggunakan defkata kunci dan memberinya nama. Ekspresi lambda memungkinkan kita untuk mendefinisikan suatu fungsi dengan lebih cepat.

Buat Fungsi Pesanan Tinggi hof_productyang mengembalikan fungsi yang mengalikan angka dengan nilai yang telah ditentukan:
```
def hof_product(multiplier):
    return lambda x: x * multiplier

mult6 = hof_product(6)
print(mult6(6)) # 36
```

### Fungsi Urutan Tinggi Bawaan

Python telah mengimplementasikan beberapa Fungsi Urutan Tinggi yang umum digunakan dari Bahasa Pemrograman Fungsional yang membuat pemrosesan objek yang dapat diulang seperti daftar dan iterator jauh lebih mudah. Untuk alasan efisiensi ruang / memori, fungsi ini mengembalikan iteratoralih - alih daftar.

### Peta

The mapFungsi memungkinkan kita untuk menerapkan fungsi untuk setiap elemen dalam suatu objek iterable. Misalnya, jika kita memiliki daftar nama dan ingin menambahkan salam ke String, kita bisa melakukan hal berikut:
```
names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)

# This prints something similar to: <map object at 0x10ed93cc0>
print(greeted_names)
# Recall, that map returns an iterator 

# We can print all names in a for loop
for name in greeted_names:
    print(name)
```

### Saring

The filterFungsi tes setiap elemen dalam suatu objek iterable dengan fungsi yang kembali baik Trueatau False, hanya menjaga mereka yang mengevaluasi untuk True. Jika kita memiliki daftar angka dan ingin menyimpan yang habis dibagi 5 kita dapat melakukan hal berikut:
```
numbers = [13, 4, 18, 35]
div_by_5 = filter(lambda num: num % 5 == 0, numbers)

# We can convert the iterator into a list
print(list(div_by_5)) # [35]
```

### Menggabungkan mapdanfilter

Karena setiap fungsi mengembalikan iterator, dan keduanya menerima objek yang dapat berulang, kita dapat menggunakannya bersama untuk manipulasi data yang sangat ekspresif!
```
# Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cube them
arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))

print(list(arbitrary_numbers)) # [27, 216, 729, 1728, 3375, 5832]
```
Ekspresi dalam arbitrary_numbersdapat dipecah menjadi 3 bagian:

* range(1, 21) adalah objek iterable yang mewakili angka dari 1, 2, 3, 4 ... 19, 20.
* filter(lambda num: num % 3 == 0, range(1, 21)) adalah iterator untuk urutan bilangan 3, 6, 9, 12, 15 dan 18.
* Saat kubik dengan mapekspresi kita bisa mendapatkan iterator untuk urutan bilangan 27, 216, 729, 1728, 3375 dan 5832.

### Daftar Pemahaman

Fitur Python populer yang muncul secara mencolok dalam Bahasa Pemrograman Fungsional adalah pemahaman daftar. Seperti fungsi mapdan filter, pemahaman daftar memungkinkan kita memodifikasi data dengan cara yang ringkas dan ekspresif.

Coba contoh sebelumnya dengan mapdan filterdengan pemahaman daftar sebagai gantinya:
```
# Recall
names = ['Shivani', 'Jan', 'Yusef', 'Sakura']
# Instead of: map(lambda x: 'Hi ' + x, names), we can do
greeted_names = ['Hi ' + name for name in names]

print(greeted_names) # ['Hi Shivani', 'Hi Jason', 'Hi Yusef', 'Hi Sakura']
```
Kesimpulan

Pemrograman Fungsional adalah paradigma pemrograman dengan perangkat lunak terutama terdiri dari fungsi pemrosesan data selama pelaksanaannya. Meskipun tidak ada satu definisi tunggal tentang apa itu Pemrograman Fungsional, kami dapat memeriksa beberapa fitur menonjol dalam Bahasa Fungsional: Fungsi Murni, Keabadian, dan Fungsi Urutan Tinggi.

Python memungkinkan kita membuat kode dengan gaya fungsional dan deklaratif. Ia bahkan memiliki dukungan untuk banyak fitur fungsional umum seperti Lambda Expressions mapdan filterfungsi dan .

link
https://github.com/praxis-academy/akademik/blob/v2.0/kurikulum/enterprise-python/isi/02.md