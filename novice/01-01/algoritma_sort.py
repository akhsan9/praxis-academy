##
d

def bubblesort(alist):
    iterasi = 0
    for j in range(len(alist)-1): #model biasa
        for i in range(len(alist)-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
        iterasi+=1
        print(iterasi,alist)
 
alist = [1,5,2,35,7,3,4]
bubblesort(alist)
print("BubbleSort",alist)

def selection(lis):
    iterasi = 0
    for i in range(len(lis)-1):
        minimal = i
        for j in range(i+1,len(lis)):
            if lis[j] < lis[minimal]:
                minimal = j
        iterasi += 1
        lis[minimal],lis[i]= lis[i],lis[minimal]
        print(iterasi,lis)
lis=[54,26,93,17,77,31,44,55,20,21,34,65,70]
selection(lis)
print("SelectionSort",lis)

def insertionsort(a):
    for j in range(len(a)-1,-1,-1):
        value = a[j]
        hole = j
        while hole<(len(a)-1) and a[hole+1]>a[hole]:
            a[hole] = a[hole+1]
            hole = hole+1
            a[hole] = value
        print(a)
a = [3,45,34,151,34,54,76,59]
insertionsort(a)
print ("insertion sort",a)

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