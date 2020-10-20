# ***Hari 5: Serialisasi Data***

Serialisasi data adalah proses mengubah data terstruktur ke dalam format yang memungkinkan berbagi atau penyimpanan data dalam bentuk yang memungkinkan pemulihan dari struktur aslinya. 

Tujuan kedua dari serialisasi data adalah untuk meminimalkan ukuran data yang kemudian mengurangi ruang disk atau kebutuhan bandwidth.

* Python menyediakan pustaka JSON bawaan untuk mengenkode dan mendekode JSON.
* Di Python 2.5, modul simplejson digunakan, sedangkan di Python 2.7, modul json digunakan. Karena penerjemah ini menggunakan Python 2.7, kami akan menggunakan json.
* Untuk menggunakan modul json, itu harus diimpor terlebih dahulu

Untuk memuat JSON kembali ke struktur data, gunakan metode "load". Metode ini mengambil string dan mengubahnya kembali menjadi struktur data objek json.

Untuk mengenkode struktur data ke JSON, gunakan metode "dumps". Metode ini mengambil objek dan mengembalikan String.

Python mendukung metode serialisasi data milik Python yang disebut pickle (dan alternatif yang lebih cepat disebut cPickle).caranya dapat digunakan dengan persis sama.

## 1. Data Flat vs. Nested data
 kedua gaya tersebut ditunjukkan pada contoh di bawah ini.

Gaya datar:
```
{ "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }
```
Gaya bertingkat:
```
{"A"
    { "field1": "value1", "field2": "value2", "field3": "value3" } }
```
## 2. Serialisasi Teks
* File sederhana (data datar)

Ini dua metode untuk membuat serial data.
repr

- Metode repr di Python mengambil satu parameter objek dan mengembalikan representasi input yang dapat dicetak:
```
# input as flat text
a =  { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

# the same input can also be read from a file
a = open('/tmp/file.py', 'r')

# returns a printable representation of the input;
# the output can be written to a file as well
print(repr(a))

# write content to files using repr
with open('/tmp/file.py') as f:f.write(repr(a))
```
- ast.literal_eval

Metode literal_eval dengan aman mem-parsing dan mengevaluasi ekspresi untuk tipe data Python. Tipe data yang didukung adalah: string, numbers, tuple, list, dicts, boolean, dan None.
```
with open('/tmp/file.py', 'r') as f: inp = ast.literal_eval(f.read())
```

## 3. File CSV (data datar)

Modul CSV di Python mengimplementasikan kelas untuk membaca dan menulis data tabel dalam format CSV.

Contoh sederhana untuk membaca:

* Reading CSV content from a file
```
import csv
with open('/tmp/file.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
Contoh sederhana untuk menulis:
```
* Writing CSV content to a file
import csv
with open('/temp/file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(iterable)
```
## 4. YAML (data bertingkat)

Ada banyak modul pihak ketiga untuk mengurai dan membaca / menulis struktur file YAML dengan Python. Salah satu contohnya ada di bawah.

```
# Reading YAML content from a file using the load method
import yaml
with open('/tmp/file.yaml', 'r', newline='') as f:
    try:
        print(yaml.load(f))
    except yaml.YAMLError as ymlexcp:
        print(ymlexcp)
```

## 5. File JSON (data bersarang)

Modul JSON Python dapat digunakan untuk membaca dan menulis file JSON. Kode contoh ada di bawah.
```
Bacaan:

# Reading JSON content from a file
import json
with open('/tmp/file.json', 'r') as f:
    data = json.load(f)

Penulisan:

# Writing JSON content to a file using the dump method
import json
with open('/tmp/file.json', 'w') as f:
    json.dump(data, f, sort_keys=True)
```

## 6. XML (data bersarang)

Penguraian XML dengan Python dapat dilakukan dengan menggunakan paket xml .
```
# reading XML content from a file
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
```

## 7. Biner
NumPy Array (data datar)

Array NumPy Python dapat digunakan untuk membuat serial dan deserialisasi data ke dan dari representasi byte.
```
import NumPy as np

# Converting NumPy array to byte format
byte_output = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]).tobytes()

# Converting byte format back to NumPy array
array_format = np.frombuffer(byte_output)
```

## 8. pickle
pickle module digunakan untuk mengimplementasikan protokol biner untuk menserialisasikan dan menghapus serialisasi/de-serialisasi struktur objek Python.

Pengawetan/pickling (dan membongkar/unpickling) secara alternatif dikenal sebagai "serialisasi", "marshalling," 1 atau "perataan"; namun, untuk menghindari kebingungan, istilah yang digunakan di sini adalah "pengawetan" dan "tidak mencabut".

* "Pengawetan/pickling" adalah proses di mana hierarki objek Python diubah menjadi aliran byte,
* "pembongkaran/unpickling" adalah operasi terbalik, di mana aliran byte (dari file biner atau objek seperti byte) diubah kembali menjadi hierarki objek. Ini adalah kebalikan dari proses Pickling di mana aliran byte diubah menjadi hierarki objek.

Antarmuka Modul:
* dumps () - Fungsi ini dipanggil untuk membuat serialisasi objek hierarki.
* load () - Fungsi ini dipanggil untuk melakukan de-serialisasi aliran data.


```
import pickle

# Berikut adalah contoh dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Gunakan dumps untuk mengonversi objeck menjadi serialized string
serial_grades = pickle.dumps( grades )

#Gunakan loads untuk membatalkan serialisasi objek
received_grades = pickle.loads( serial_grades )
```


## 9. Serialization JSON vs XML

Baik JSON dan XML dapat digunakan untuk menerima data dari server web.


Contoh JSON
```
{
  "MenteriKordinator": [ 
	
     { 
        "id":"A001", 
        "namaLengkap": "Mohammad Mahfud Md", 
        "bidang": "Politik, Hukum, dan Keamanan" 
     }, 
	
     { 
        "id":"A002", 
        "name": "Airlangga Hartarto", 
        "bagian": "Perekonomian" 
     },

     { 
      "id":"A003", 
      "name": "Muhadjir Effendy", 
      "bagian": "Pembangunan Manusia dan Kebudayaan" 
     }, 
     { 
      "id":"A004", 
      "name": "Luhut Binsar Pandjaitan", 
      "bagian": "Kemaritiman dan Investasi" 
     } 
  ]   
}
```
Contoh XML
```
<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<MenteriKordinator>
		<id>A001</id>
		<namaLengkap>Mohammad Mahfud Md</namaLengkap>
		<bagian>Politik, Hukum, dan Keamanan</bagian>
  <MenteriKordinator/>
  <MenteriKordinator>
		<id>A001</id>
		<namaLengkap>Airlangga Hartarto</namaLengkap>
		<bagian>Perekonomian</bagian>
  <MenteriKordinator/>
  <MenteriKordinator>
		<id>A001</id>
		<namaLengkap>Muhadjir Effendy</namaLengkap>
		<bagian>Pembangunan Manusia dan Kebudayaan</bagian>
  <MenteriKordinator/>
  <MenteriKordinator>
		<id>A001</id>
		<namaLengkap>Luhut Binsar Pandjaitan</namaLengkap>
		<bagian>Kemaritiman dan Investasi</bagian>
  <MenteriKordinator/>
</root>
```
JSON Seperti XML Karena

    * Baik JSON dan XML "mendeskripsikan diri sendiri" (dapat dibaca manusia)
    * Baik JSON dan XML bersifat hierarki (nilai di dalam nilai)
    * Baik JSON dan XML dapat diurai dan digunakan oleh banyak bahasa pemrograman
    * Baik JSON maupun XML dapat diambil dengan XMLHttpRequest

JSON Tidak Seperti XML Karena

    * JSON tidak menggunakan tag akhir
    * JSON lebih pendek
    * JSON lebih cepat untuk membaca dan menulis
    * JSON dapat menggunakan array

Perbedaan terbesarnya adalah:

XML harus diurai dengan parser XML. JSON dapat diurai dengan fungsi JavaScript standar.

Mengapa JSON Lebih Baik Dari XML
```
XML jauh lebih sulit untuk diurai daripada JSON.
JSON diurai menjadi objek JavaScript yang siap digunakan.
```
Untuk aplikasi AJAX, JSON lebih cepat dan lebih mudah daripada XML:

Menggunakan XML

    * Ambil dokumen XML
    * Gunakan XML DOM untuk melewati dokumen
    * Ekstrak nilai dan simpan dalam variabel

Menggunakan JSON

    * Ambil string JSON
    * JSON. Parse string JSON


