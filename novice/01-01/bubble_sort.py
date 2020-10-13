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

from bubble_sort import bubbleSort as bb
arr = [71, 64,53,40]

print(arr)
print(bb(arr))