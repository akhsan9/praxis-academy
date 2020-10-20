import json

with open('novice/01-05/karyawan.json') as data_student:

    data = json.load(data_student)

murid = data['MenteriKordinator']

print(data)


from bs4 import BeautifulSoup

with open('novice/01-05/karyawan.xml', 'r') as data_student:
	data = data_student.read()

MenteriKordinator = BeautifulSoup(data, 'xml')
print(MenteriKordinator)