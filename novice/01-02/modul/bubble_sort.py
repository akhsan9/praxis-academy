
# Implementasi Bubble Sort

def bubbleSort(val):
	n = len(val)

	# Melintasi semua elemen array
	for i in range(n):

# Elemen i terakhir sudah ada
		for j in range(0, n-i-1):

			# melintasi array dari 0 ke n-i-1
            # Tukar jika elemen yang ditemukan lebih besar
            # daripada elemen berikutnya
			if val[j] > val[j+1] :
				val[j], val[j+1] = val[j+1], val[j]
	return val