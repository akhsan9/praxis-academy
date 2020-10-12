
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

    Di Windows 4 :

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


