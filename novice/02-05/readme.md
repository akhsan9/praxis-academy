# ***Hari 5: DBMS: SQL dan ORM***

## 1. Database

Sebuah Database adalah sebuah koleksi terorganisir dari data yang umumnya disimpan dan diakses secara elektronik dari sistem komputer. Dimana database lebih kompleks, mereka sering dikembangkan dengan menggunakan desain formal dan teknik pemodelan . 

Sistem manajemen basis data (DBMS) adalah perangkat lunak yang berinteraksi dengan pengguna akhir , aplikasi, dan basis data itu sendiri untuk menangkap dan menganalisis data. Perangkat lunak DBMS juga mencakup fasilitas inti yang disediakan untuk mengelola database. Jumlah total database, DBMS dan aplikasi terkait dapat disebut sebagai "sistem database". Seringkali istilah "database" juga digunakan untuk merujuk ke salah satu DBMS, sistem database atau aplikasi yang terkait dengan database. 

Connolly dan Begg mendefinisikan sistem manajemen basis data (DBMS) sebagai "sistem perangkat lunak yang memungkinkan pengguna untuk mendefinisikan, membuat, memelihara, dan mengontrol akses ke basis data". Contoh DBMS termasuk MySQL , PostgreSQL , MSSQL , Oracle Database , dan Microsoft Access . 

Fungsionalitas yang disediakan oleh DBMS dapat sangat bervariasi. Fungsionalitas inti adalah penyimpanan, pengambilan, dan pembaruan data. Codd mengusulkan fungsi dan layanan berikut yang harus disediakan oleh DBMS untuk keperluan umum: [25]

* Penyimpanan, pengambilan dan pembaruan data
* Katalog yang dapat diakses pengguna atau kamus data yang menjelaskan metadata
* Dukungan untuk transaksi dan konkurensi
* Fasilitas untuk memulihkan database jika rusak
* Dukungan untuk otorisasi akses dan pembaruan data
* Akses dukungan dari lokasi terpencil
* Menerapkan batasan untuk memastikan data dalam database mematuhi aturan tertentu

Secara umum juga diharapkan DBMS akan menyediakan sekumpulan utilitas untuk tujuan yang mungkin diperlukan untuk mengelola database secara efektif, termasuk impor, ekspor, pemantauan, defragmentasi, dan utilitas analisis. [26] Bagian inti dari DBMS yang berinteraksi antara database dan antarmuka aplikasi terkadang disebut sebagai mesin database . 

### Bahasa database

Bahasa database adalah bahasa tujuan khusus, yang memungkinkan satu atau beberapa tugas berikut, terkadang dibedakan sebagai subbahasa :

* Bahasa kontrol data (DCL) - mengontrol akses ke data;
* Bahasa definisi data (DDL) - mendefinisikan tipe data seperti membuat, mengubah, atau menghapus tabel dan hubungan di antara mereka;
* Bahasa manipulasi data (DML) - melakukan tugas-tugas seperti memasukkan, memperbarui, atau menghapus kejadian data;
* Bahasa kueri data (DQL) - memungkinkan pencarian informasi dan komputasi informasi turunan.

Bahasa database dikhususkan untuk model data tertentu. Contoh penting termasuk:

 * SQL menggabungkan peran definisi data, manipulasi data, dan kueri dalam satu bahasa. Ini adalah salah satu bahasa komersial pertama untuk model relasional, meskipun dalam beberapa hal ia berangkat dari model relasional seperti yang dijelaskan oleh Codd (misalnya, baris dan kolom tabel dapat diurutkan). SQL menjadi standar American National Standards Institute (ANSI) pada tahun 1986, dan dari Organisasi Internasional untuk Standardisasi (ISO) pada tahun 1987. Sejak itu standar telah ditingkatkan secara teratur dan didukung (dengan berbagai tingkat kesesuaian) oleh semua komersial utama DBMS relasional. [29] [30]
* OQL adalah standar bahasa model objek (dari Object Data Management Group ). Ini telah memengaruhi desain beberapa bahasa kueri yang lebih baru seperti JDOQL dan EJB QL .
* XQuery adalah bahasa query XML standar yang diimplementasikan oleh sistem database XML seperti MarkLogic dan eXist , oleh database relasional dengan kemampuan XML seperti Oracle dan DB2, dan juga oleh prosesor XML dalam memori seperti Saxon .
* SQL / XML menggabungkan XQuery dengan SQL. [31]

Bahasa database juga dapat menggabungkan fitur-fitur seperti:

* Konfigurasi khusus DBMS dan manajemen mesin penyimpanan
* Perhitungan untuk mengubah hasil kueri, seperti menghitung, menjumlahkan, rata-rata, menyortir, mengelompokkan, dan referensi silang
* Penerapan batasan (misalnya dalam database otomotif, hanya mengizinkan satu jenis mesin per mobil)
* Versi antarmuka pemrograman aplikasi dari bahasa query, untuk kenyamanan programmer



## 2. Bagaimana menghubungkan program Python ke MariaDB





https://github.com/praxis-academy/akademik/blob/v2.0/kurikulum/enterprise-python/isi/02.md