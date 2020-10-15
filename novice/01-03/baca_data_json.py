# gunakan modul json
import json

# buka file JSON
file_json = open("turis.json")

# prsing data JSON
data = json.loads(file_json.read())

# cetak isi data JSON
print(data)