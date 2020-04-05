import time
from datetime import date

print('------------------------------------------------')
print('--------------DATA BRIZZI & no HP---------------')
print('------------------------------------------------')

while True:
	myfile = open('data.txt', 'r')

	file = myfile.read()
	file = file.replace(' | ', ' ')
	file = file.replace('\n', ' ')
	file = file.split(" ")
	file.remove('')
	brizz = input('Masukkan No Brizzi\t: ')
	if brizz in file:
		print('Nomor Brizzi telah digunakan')
	
		continue
	else:	
		hp = int(input('Masukkan No.HP\t\t: +62'))
		va = input('Masukkan nomer va\t: ')
		passw = input('Masukkan Pasword\t: ')
		time.sleep(1)


	

	print('\n---------Data telah berhasil ditambahkan--------\n')
	jawab = input("ulangi input lagi? (y/n) ")

	if jawab == 'y':
		file = open('data.txt', 'a')
		skrg = date.today()
		file.write("{} | {} | {} | {} | {}\n".format(brizz, hp, va, passw, skrg))
		file.close()
		continue
	elif jawab == 'n':
		file = open('data.txt', 'a')
		skrg = date.today()
		file.write("{} | {} | {} | {} | {}\n".format(brizz, hp, va, passw, skrg))
		file.close()
		time.sleep(1)
		print('-----------------Terima Kasih ^^----------------')
		time.sleep(1)
		print('\nMasukkan Perintah python search.py untuk mencari\n')
		time.sleep(1)		
		break
	else:
		print('input tidak valid')
		break
