
```### Hari 1: Python ```
<blockquote>
  <p>Dasar-dasar python</p>
</blockquote>

1. Pembahasan interpreter dan compiler

    Bahasa pemrograman adalah bahasa formal yang terdiri dari set instruksi yang menghasilkan berbagai macam keluaran yang digunakan untuk mengimplementasikan algoritma . 
    Kebanyakan bahasa pemrograman terdiri dari instruksi untuk komputer .
    Sebuah implementasi dari bahasa pemrograman menyediakan cara untuk menulis program dalam bahasa itu dan mengeksekusi mereka pada satu atau lebih konfigurasi hardware dan software. 
    Secara umum, ada dua pendekatan untuk implementasi bahasa pemrograman: kompilasi dan interpretasi . 

    Compiler atau Kompilator adalah program komputer yang menerjemahkan kode komputer yang ditulis dalam satu bahasa pemrograman ( bahasa sumber ) ke bahasa lain ( bahasa target ). Nama "compiler" terutama digunakan untuk program yang menerjemahkan kode sumber dari bahasa pemrograman tingkat tinggi ke bahasa tingkat yang lebih rendah (misalnya, PHP, Python, Ruby and Lua.)

    Interpreter adalah program komputer yang secara langsung menjalankan instruksi yang ditulis dalam bahasa pemrograman atau scripting , tanpa mengharuskannya sebelumnya telah dikompilasi ke dalam program bahasa mesin

2. Programing tool
    
    Adalah program komputer dimana software development yang gunakan untuk membuat'create', debug, maintain, atau mendukung program lain dan aplikasi. 

3. Implementasi Python
    
    CPython adalah implementasi referensi dari Python yang ditulis di bahasa C,CPython mengkompilasi program Python menjadi bytecode perantara yang kemudian dieksekusi oleh virtual machine.

    PyPy adalah interpreter Python 2.7 dan 3.6 yang cepat dan sesuai. tetapi pada library yang ditulis dalam C tidak dapat digunakan dengan PyPy.

    Stackless Python adalah fork penting dari CPython yang mengimplementasikan microthreads itu tidak menggunakan tumpukan memori bahasa C, sehingga memungkinkan program bersamaan secara masif. PyPy juga memiliki versi tanpa tumpukan'stackless'. 

    MicroPython dan CircuitPython adalah varian Python 3 yang dioptimalkan untuk mikrokontroler . Ini termasuk Lego Mindstorms EV3 .

  4. Riwayat versi dari Python.
      
      Rilis sebelum versi implementasi dimulai - Desember 1989
      Rilis internal di Centrum Wiskunde & Informatica - 1990
- versi sampai  [] tanggal rilis[]

- 0.9     0.9.9 []  1991-02-20 []
- 1.0 	  1.0.4 [] 	1994-01-26 []
- 1.1 	  1.1.1 [] 	1994-10-11 [] 	
- 1.2 	  -.-.- []  1995-04-13 []
- 1.3     -.-.- []	1995-10-13 [] 	
- 1.4 		-.-.- []  1996-10-25 [] 
- 1.5 	  1.5.2 [] 	1998-01-03 [] 	
- 1.6 	  1.6.1 [] 	2000-09-05 [] 
- 2.0 	  2.0.1 [] 	2000-10-16 [] 
- 2.1 	  2.1.3 [] 	2001-04-15 [] 
- 2.2 	  2.2.3 [] 	2001-12-21 [] 
- 2.3 	  2.3.7 [] 	2003-06-29 [] 
- 2.4 	  2.4.6 [] 	2004-11-30 [] 
- 2.5 	  2.5.6 [] 	2006-09-19 []
- 2.6 	  2.6.9 [] 	2008-10-01 [] 
- 2.7 	  2.7.18[] 	2010-07-03 [] 
- 3.0 	  3.0.1 [] 	2008-12-03 [] 
- 3.1 	  3.1.5 [] 	2009-06-27 [] 
- 3.2 	  3.2.6 [] 	2011-02-20 [] 
- 3.3 	  3.3.7 [] 	2012-09-29 [] 
- 3.4 	  3.4.10[] 	2014-03-16 [] 	
- 3.5 	  3.5.10[] 	13-09-2015 [] 	
- 3.6 	  3.6.12[] 	23-12-2016 [] 
- 3.7 	  3.7.9 [] 	2018-06-27 [] 
- 3.8 	  3.8.6 [] 	2019-10-14 [] 
- 3.9 	  3.9.0 [] 	2020-10-05 [] 
- 3.10 		-.-.- []  2021-10-25 []

 5. Instalasi

    pip sudah diinstal jika Anda menggunakan Python 2> = 2.7.9 atau Python 3> = 3.4 diunduh dari python.org atau jika Anda bekerja di Lingkungan Virtual yang dibuat oleh virtualenv atau pyvenv . Pastikan untuk mengupgrade pip .

    Untuk menginstal pip, unduh 1 secara aman get-pip.pydengan mengikuti tautan ini: get-pip.py . Alternatifnya, gunakan curl:

    Menginstal dengan get-pip.py
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```

    Kemudian jalankan perintah berikut di folder tempat Anda mengunduh get-pip.py:
    ```
    python get-pip.py
    ```

    Meningkatkan pip di Linux atau macOS:

    ```
    pip install -U pip
    ```

    Di Windows NT 4.0 :

    ``` 
    python -m pip install -U pip 
    ```
    untuk ysng menggunakan pip3
* sudo apt update #untuk update harian
* python3 get-pip.py #untuk memilih pip
* sudo apt install python3-pip
* python --version
* python3 --version
* pip3 --version
* pip3 install jupyterlab
* pip3 install notebook

 tambahan
* pip3 install voila,
* pip3 install numpy


6. algoritma short

* Bubble sort

    Bubble sort (metode gelembung) adalah metode/algoritma pengurutan dengan dengan cara melakukan penukaran data dengan tepat disebelahnya secara terus menerus sampai bisa dipastikan dalam satu iterasi tertentu tidak ada lagi perubahan.

```
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
 
DaftarAngka = [20,5,30,100,3,25,9,17]
BubbleSort(DaftarAngka)
print("BubbleSort",DaftarAngka)
hasil
BubbleSort [3, 5, 9, 17, 20, 25, 30, 100]
```

* Selection sort
Selection Sort adalah sorting dengan prinsip memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke-i. Nilai dari i dimulai dari 1 ke n, dimana n adalah julah total elemen dikurangi 1.

```
def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print("SelectionSort",DaftarAngka)
hasil
SelectionSort [4, 7, 11, 15, 20, 23, 32, 99]

```

* Inserttion sort

Insertion sort adalah sebuah metode pengurutan data dengan menempatkan setiap elemen data pada pisisinya dengan cara melakukan perbandingan dengan data – data yang ada.
```

def InsertionSort(val):
   for index in range(1,len(val)):
 
     valueaktif = val[index]
     posisi = index
 
     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1
 
     val[posisi]=valueaktif
 
DaftarAngka = [23,7,32,99,4,15,11,20]
InsertionSort(DaftarAngka)
print("InsertionSort",DaftarAngka)
hasil 
insertion sort [151, 76, 59, 54, 45, 34, 34, 3]
```

* Quick sort

Quicksort merupakan Algoritme Pembagi. Pertama quicksort membagi list yang besar menjadi dua buah sub list yang lebih kecil: element kecil dan element besar. Quicksort kemudian dapat menyortir sub list itu secara rekursif. 
```
def quickshort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quickshort(a,start,pindex-1)
        quickshort(a,pindex+1,end)
 
def partition(a,start,end):
    middle = int(end/2)
    pivot = a[middle]
    pindex = start
    for i in range(start,middle):
        if a[i]>=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex = pindex + 1
    a[pindex],a[middle]=a[middle],a[pindex]
    print(a)
    return pindex
 
a = [5, 9, 4, 2, 3]
quickshort(a,0,len(a)-1)
hasil
[5, 9, 4, 2, 3]
[5, 9, 4, 2, 3]
[5, 9, 2, 4, 3]
```

* Merged Sort

Merge Sort adalah salah satu sorting dengan metode memecah data kemudian menyelesaikannya setiap bagian dan menggabungkannya kembali hingga data terurut.
```
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

hasil
Splitting  [54, 26, 93, 17, 77, 31, 44, 55, 20]
Splitting  [54, 26, 93, 17]
Splitting  [54, 26]
Splitting  [54]
Merging  [54]
Splitting  [26]
Merging  [26]
Merging  [26, 54]
Splitting  [93, 17]
Splitting  [93]
Merging  [93]
Splitting  [17]
Merging  [17]
Merging  [17, 93]
Merging  [17, 26, 54, 93]
Splitting  [77, 31, 44, 55, 20]
Splitting  [77, 31]
Splitting  [77]
Merging  [77]
Splitting  [31]
Merging  [31]
Merging  [31, 77]
Splitting  [44, 55, 20]
Splitting  [44]
Merging  [44]
Splitting  [55, 20]
Splitting  [55]
Merging  [55]
Splitting  [20]
Merging  [20]
Merging  [20, 55]
Merging  [20, 44, 55]
Merging  [20, 31, 44, 55, 77]
Merging  [17, 20, 26, 31, 44, 54, 55, 77, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
```