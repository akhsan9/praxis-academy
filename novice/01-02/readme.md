### Hari 2: Dasar-dasar Pemrograman Python (2)

1. Struktur data di Python
    ```
     *list/dafar tumpukan: 
     list.append -menambahkan item ke akhir daftar., 
        stack = [3, 4, 5]
        stack.append(6)
        stack.append(7)
        print (stack)

     *del/untuk menghapus item: 
        #untuk delete urutan ke-0
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[0]
        print (a)
        hasilnya "[1, 66.25, 333, 333, 1234.5]"

     *Queues/menggunakan data sebagai antrian:
        from collections import deque
        queue = deque(["Eric", "John", "Michael"])
        queue.append("Terry")           
        queue.append("Graham")          
        print (queue.popleft()) #hasil Eric
        print (queue) #hasil deque(['John', 'Michael', 'Terry', 'Graham'])

      *from collections import deque
        queue = deque(["ibran", "adi", "iqlima"])
        queue.append("alan")           
        queue.append("rino")          
        print (queue.popleft()) 
        print (queue)

        basket = {'apel', 'jeruk', 'apel', 'pear', 'jeruk', 'banana'}
        print(basket)                      # untuk menampilkan gandaan yang dihapus
        {'pear', 'banana', 'apel', 'jeruk'}
        print ('apel' in basket)            # untuk mempercepat test member
        true
        print ('salak' in basket)
        false
    *dictionary list untuk mencari di kamus
        dic = {'jack': 4098, 'sape': 4139}
        dic['guido'] = 4127
        print (dic)
        {'jack': 4098, 'sape': 4139, 'guido': 4127}

    

    ```
2. *Modules* di Python
    Pernyataan from..import 
    ```
    from math import sqrt
    print("Square root dari 16 yaitu", sqrt(16))
    hasil
    Square root dari 16 yaitu 4.0
    ```
    Sebuah modul __name__ 
    ```
    if __name__ == '__main__':
    print('Program ini dijalankan dengan sendirinya')
    else:
    print ('program ini sedang diimpor dari modul lain')
    ```
    Membuat dir bekerja
    ```
    


3. Input Output di Python
4. Penanganan *errors dan exceptions*.

