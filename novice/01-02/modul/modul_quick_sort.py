# implementasi dari Quicksort Sort 

# Fungsi ini mengambil elemen terakhir sebagai pivot, 
# tempat elemen pivot pada posisi yang benar dalam urutan larik, 
# dan tempatkan semuanya lebih kecil (lebih kecil dari pivot) 
# di kiri pivot dan semua elemen besar di kanan pivot 

def partition(arr,low,high): 
	i = ( low-1 )		 # indeks elemen yang lebih kecil
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# Jika elemen saat ini lebih kecil dari pivot
		if arr[j] < pivot: 
		
			# indeks kenaikan dari elemen yang lebih kecil
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

#  Fungsi utama yang mengimplementasikan QuickSort 
# arr[] --> Array to be sorted(urutkan), 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi adalah indeks partisi, arr [p] sekarang di tempat yang tepat
		pi = partition(arr,low,high) 

		# Sebelumnya urutkan elemen secara terpisah partisi dan setelah partisi 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code untuk diuji di atas 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 

# This code is contributed by Mohit Kumra 