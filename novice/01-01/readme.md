# Minggu 01

## Hari 1: Python, Ekosistem Python, dan Dasar-dasar Pemrograman Python

### Pembelajaran

```
Materi dan Penjelasan
```

1. Keterkaitan antara [bahasa pemrograman](https://en.wikipedia.org/wiki/Programming_language), [compiler](https://en.wikipedia.org/wiki/Compiler), dan [interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing)).

    Sebuah bahasa pemrograman adalah bahasa formal yang terdiri dari set instruksi yang menghasilkan berbagai macam keluaran . Bahasa pemrograman digunakan dalam pemrograman komputer untuk mengimplementasikan algoritma . 
    Kebanyakan bahasa pemrograman terdiri dari instruksi untuk komputer .
    Sebuah implementasi dari bahasa pemrograman menyediakan cara untuk menulis program dalam bahasa itu dan mengeksekusi mereka pada satu atau lebih konfigurasi hardware dan software. Secara umum, ada dua pendekatan untuk implementasi bahasa pemrograman: kompilasi dan interpretasi . Secara umum dimungkinkan untuk mengimplementasikan bahasa menggunakan salah satu teknik.

      Dalam komputasi , kompilator adalah program komputer yang menerjemahkan kode komputer yang ditulis dalam satu bahasa pemrograman ( bahasa sumber ) ke bahasa lain ( bahasa target ). Nama "compiler" terutama digunakan untuk program yang menerjemahkan kode sumber dari bahasa pemrograman tingkat tinggi ke bahasa tingkat yang lebih rendah (misalnya, PHP, Python, Ruby and Lua.)

    Implementasi dari bahasa pemrograman menyediakan cara untuk menulis program dalam bahasa itu dan mengeksekusi mereka pada satu atau lebih konfigurasi hardware dan software. Secara umum, ada dua pendekatan untuk implementasi bahasa pemrograman: kompilasi dan interpretasi . Secara umum dimungkinkan untuk mengimplementasikan bahasa menggunakan salah satu teknik.

     interpreter adalah program komputer yang secara langsung menjalankan instruksi yang ditulis dalam bahasa pemrograman atau scripting , tanpa mengharuskannya sebelumnya telah dikompilasi ke dalam program bahasa mesin

Output dari kompilator dapat dieksekusi oleh perangkat keras atau program yang disebut juru bahasa. Dalam beberapa implementasi yang menggunakan pendekatan interpreter, tidak ada batasan yang jelas antara kompilasi dan interpreting. Misalnya, beberapa implementasi BASIC mengkompilasi dan kemudian mengeksekusi sumber baris pada satu waktu. 
2. Komponen dari [peranti pengembangan (*development tools*)](https://en.wikipedia.org/wiki/Programming_tool) dan bisa mencari komponen-komponen untuk suatu bahasa pemrograman tertentu.
3. Keterkaitan antara [Python sebagai bahasa pemrograman](https://en.wikipedia.org/wiki/Python_(programming_language)) dengan [implementasi Python](https://en.wikipedia.org/wiki/Python_(programming_language)#Implementations).

  CPython adalah implementasi referensi dari Python. 
  <table class="wikitable"><caption><font style="vertical-align: inherit;"><font style="vertical-align: inherit;" class="">Ringkasan tipe bawaan Python 3
</font></font></caption>
<tbody><tr><th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tipe
</font></font></th>
<th><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Immutable_object&amp;usg=ALkJrhgsXs19fC4vkp_KqK9epyV4WArxmQ" title="Objek yang tidak berubah"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;" class="">Mutabilitas</font></font></a>
</th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Deskripsi
</font></font></th>
<th style="width: 23em;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contoh sintaks
</font></font></th></tr><tr><td><code>bool</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Boolean_value&amp;usg=ALkJrhjheR9q1u6HkN6xMpYKcVv9Sdo9KQ" class="mw-redirect" title="Nilai Boolean"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Nilai Boolean</font></font></a>
</td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="kc">True</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="kc">False</span></code>
</td></tr><tr><td><code>bytearray</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">yg mungkin berubah
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Urutan </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Byte&amp;usg=ALkJrhh4O_PjNNc1rcrEAEnpTwpqpLou0A" title="Byte"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">byte</font></font></a>
</td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">bytearray</span><span class="p">(</span><span class="sa">b</span><span class="s1">'Some ASCII'</span><span class="p">)</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">bytearray</span><span class="p">(</span><span class="sa">b</span><span class="s2">"Some ASCII"</span><span class="p">)</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">bytearray</span><span class="p">([</span><span class="mi">119</span><span class="p">,</span> <span class="mi">105</span><span class="p">,</span> <span class="mi">107</span><span class="p">,</span> <span class="mi">105</span><span class="p">])</span></code>
</td></tr><tr><td><code>bytes</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Urutan byte
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="sa">b</span><span class="s1">'Some ASCII'</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="sa">b</span><span class="s2">"Some ASCII"</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">bytes</span><span class="p">([</span><span class="mi">119</span><span class="p">,</span> <span class="mi">105</span><span class="p">,</span> <span class="mi">107</span><span class="p">,</span> <span class="mi">105</span><span class="p">])</span></code>
</td></tr><tr><td><code>complex</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Complex_number&amp;usg=ALkJrhiNyeBb-ztf5wLTwUPT9H3OwcrVew" title="Bilangan kompleks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Bilangan kompleks</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> dengan bagian nyata dan imajiner
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="mi">3</span><span class="o">+</span><span class="mf">2.7</span><span class="n">j</span></code>
</td></tr><tr><td><code>dict</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">yg mungkin berubah
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Associative_array&amp;usg=ALkJrhiQre30xeCLeXuLI9Fjo6ZURHhxuw" title="Array asosiatif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Array asosiatif</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> (atau kamus) pasangan kunci dan nilai; </font><font style="vertical-align: inherit;">dapat berisi jenis campuran (kunci dan nilai), kunci harus berupa jenis yang dapat dicirikan
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">{</span><span class="s1">'key1'</span><span class="p">:</span> <span class="mf">1.0</span><span class="p">,</span> <span class="mi">3</span><span class="p">:</span> <span class="kc">False</span><span class="p">}</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">{}</span></code>
</td></tr><tr><td><code>ellipsis</code><sup class="reference plainlinks nourlexpansion" id="ref_inaccessible-type"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#endnote_inaccessible-type"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah</font></font></a></sup></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Ellipsis_(programming_operator)&amp;usg=ALkJrhhkl0cLQn7Ho1FPY9C86dSoJ-0aHw" class="mw-redirect" title="Ellipsis (operator pemrograman)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">elipsis</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> placeholder untuk digunakan sebagai indeks dalam </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/NumPy&amp;usg=ALkJrhjl2BUNy2N_Cd3tO5M5EPo1VT0y-Q" title="NumPy"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">NumPy</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> array
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="o">...</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="bp">Ellipsis</span></code>
</td></tr><tr><td><code>float</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Double_precision&amp;usg=ALkJrhjEuAxSzw_3MY61dPfnAJlv-nC5lQ" class="mw-redirect" title="Presisi ganda"><font style="vertical-align: inherit;"></font></a> <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Angka </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Floating_point&amp;usg=ALkJrhjhyc3BghZC8QW2cT7BbyZpO7x5qQ" class="mw-redirect" title="Titik apung"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">floating point </font></font></a><font style="vertical-align: inherit;"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Double_precision&amp;usg=ALkJrhjEuAxSzw_3MY61dPfnAJlv-nC5lQ" class="mw-redirect" title="Presisi ganda"><font style="vertical-align: inherit;">presisi ganda</font></a><font style="vertical-align: inherit;"> . </font><font style="vertical-align: inherit;">Presisi bergantung pada mesin tetapi dalam praktiknya umumnya diimplementasikan sebagai angka </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/IEEE_754&amp;usg=ALkJrhgzp_PowCKHo7LPBLEfAJtyJv2ypg" title="IEEE 754"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">IEEE 754</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 64-bit </font><font style="vertical-align: inherit;">dengan presisi 53 bit </font></font><sup id="cite_ref-87" class="reference"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#cite_note-87"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[87]</font></font></a></sup></td>
<td>
<p><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="mf">1.414</span></code>
</p>
</td></tr><tr><td><code>frozenset</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Set_(computer_science)&amp;usg=ALkJrhh3x2QDg7McFuvP2Nuc5UiEZjq6Xg" class="mw-redirect" title="Set (ilmu komputer)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Set tidak</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> berurutan </font><font style="vertical-align: inherit;">, tidak berisi duplikat; </font><font style="vertical-align: inherit;">dapat berisi tipe campuran, jika memiliki hash
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">frozenset</span><span class="p">([</span><span class="mf">4.0</span><span class="p">,</span> <span class="s1">'string'</span><span class="p">,</span> <span class="kc">True</span><span class="p">])</span></code>
</td></tr><tr><td><code>int</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Integer_(computer_science)&amp;usg=ALkJrhjewTC5iCJ0DxUquKHQaqoF_MN9vA" title="Integer (ilmu komputer)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Bilangan</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> bulat dengan besaran tak terbatas </font></font><sup id="cite_ref-pep0237_88-0" class="reference"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#cite_note-pep0237-88"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[88]</font></font></a></sup></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="mi">42</span></code>
</td></tr><tr><td><code>list</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">yg mungkin berubah
</font></font></td>
<td><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/List_(computer_science)&amp;usg=ALkJrhhv6SmZIRXTJsqi9v-G6hDJB_MhUg" class="mw-redirect" title="Daftar (ilmu komputer)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Daftar</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> , dapat berisi jenis campuran
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">[</span><span class="mf">4.0</span><span class="p">,</span> <span class="s1">'string'</span><span class="p">,</span> <span class="kc">True</span><span class="p">]</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">[]</span></code>
</td></tr><tr><td><code>NoneType</code><sup class="reference plainlinks nourlexpansion" id="ref_inaccessible-type"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#endnote_inaccessible-type"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah</font></font></a></sup></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Objek yang merepresentasikan ketiadaan nilai, sering disebut </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Null_pointer&amp;usg=ALkJrhiRS0OEgh6gK7FPVkdSDRbP4ANWEg" title="Pointer nol"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">null</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> dalam bahasa lain
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="kc">None</span></code>
</td></tr><tr><td><code>NotImplementedType</code><sup class="reference plainlinks nourlexpansion" id="ref_inaccessible-type"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#endnote_inaccessible-type"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah</font></font></a></sup></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Placeholder yang dapat dikembalikan dari </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Operator_overloading&amp;usg=ALkJrhji2PD6g-2KvmVS5NSGIXIvB-ToWQ" title="Operator kelebihan beban"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">operator yang kelebihan beban</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> untuk menunjukkan jenis operan yang tidak didukung.
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="bp">NotImplemented</span></code>
</td></tr><tr><td><code>range</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah Urutan angka yang biasa digunakan untuk mengulang beberapa kali dalam </font></font><code>for</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">loop </font></font><sup id="cite_ref-89" class="reference"><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Python_(programming_language)&amp;usg=ALkJrhhLtFWH4TSW_yvEGCARf5B2eylUTQ#cite_note-89"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[89]</font></font></a></sup></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">)</span></code>
</td></tr><tr><td><code>set</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">yg mungkin berubah
</font></font></td>
<td><font style="vertical-align: inherit;"></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/Set_(computer_science)&amp;usg=ALkJrhh3x2QDg7McFuvP2Nuc5UiEZjq6Xg" class="mw-redirect" title="Set (ilmu komputer)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Set tidak</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> berurutan </font><font style="vertical-align: inherit;">, tidak berisi duplikat; </font><font style="vertical-align: inherit;">dapat berisi tipe campuran, jika memiliki hash
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">{</span><span class="mf">4.0</span><span class="p">,</span> <span class="s1">'string'</span><span class="p">,</span> <span class="kc">True</span><span class="p">}</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="nb">set</span><span class="p">()</span></code>
</td></tr><tr><td><code>str</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sebuah </font></font><a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=id&amp;pto=aue&amp;rurl=translate.google.co.id&amp;sl=auto&amp;sp=nmt4&amp;tl=id&amp;u=https://en.m.wikipedia.org/wiki/String_(computer_science)&amp;usg=ALkJrhiBPfim5Bi3hpU4bH4-eWv1oUiINQ" title="String (ilmu komputer)"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">karakter string</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : urutan codepoints Unicode
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="s1">'Wikipedia'</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="s2">"Wikipedia"</span></code><br><div class="mw-highlight mw-highlight-lang-python mw-content-ltr" dir="ltr"><pre><span></span><span class="sd"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">"" "Mencakup </font></font></span>
<span class="sd"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">banyak </font></font></span>
<span class="sd"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">baris" ""</font></font></span>
</pre></div>
</td></tr><tr><td><code>tuple</code>
</td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">kekal
</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Bisa berisi tipe campuran
</font></font></td>
<td><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">(</span><span class="mf">4.0</span><span class="p">,</span> <span class="s1">'string'</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">(</span><span class="s1">'single element'</span><span class="p">,)</span></code><br><code class="mw-highlight mw-highlight-lang-python" id="" style="" dir="ltr"><span class="p">()</span></code>
</td></tr></tbody></table>

4. [Riwayat versi dari Python](https://en.wikipedia.org/wiki/History_of_Python).
Python adalah bahasa pemrograman yang ditafsirkan , tingkat tinggi , dan tujuan umum . Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, Python dibuat pada akhir 1980-an sebagai penerus bahasa ABC . Python 2.0, dirilis pada tahun 2000, Bahasa Python 2 secara resmi dihentikan pada tahun 2020 (pertama kali direncanakan pada tahun 2015), dan "Python 2.7.18 adalah rilis terakhir Python 2.7 dan oleh karena itu merupakan rilis terakhir Python 2. 


5. [Manual pip](https://pip.pypa.io/en/stable/). ####Instalasi python "pip3"
1. sudo apt update - untuk update harian
2. python get-pip.py untuk memilih pip
3. sudo apt install python3-pip
4. python --version
5. python3 --version
6. pip3 --version
7. pip3 install jupyterlab
8. pip3 install notebook
- tambahan
pip3 install voila,
pip3 install numpy

Pemakaian:
  pip3 <perintah> [opsi]


