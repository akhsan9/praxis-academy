import textwrap
doc = """Metode wrap () sama seperti fill () kecuali metode ini mengembalikan
daftar string, bukan satu string besar dengan baris baru untuk dipisahkan
garis yang dibungkus."""

print('ini di file',(textwrap))
print(textwrap.fill(doc, width=40))