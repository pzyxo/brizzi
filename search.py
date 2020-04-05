import time

print('------------------------------------------------')
print('--------------DATA BRIZZI & no HP---------------')
print('------------------------------------------------')


myfile = open('data.txt', 'r')

file = myfile.read()
file = file.replace(' | ', ' ')
file = file.replace('\n', ' ')
file = file.split(" ")
file.remove('')
while True:

	menu = int(input('\nMau cari lewat apa?\n1. nomer hp\n2. nomer brizzi\n\n'))
	if menu == 1:	
		cari = input('Masukkan nomer hp : +62')

		if cari in file:
			a = file.index(cari)
			print('Data Tokopedia x Brizzi')
			print('Loading...')
			time.sleep(2)
			print('Nomor HP\t\t: +62', file[a])
			time.sleep(1)
			print('Nomor Brizzi\t\t:', file[a-1])
			time.sleep(1)
			print('Nomor VA\t\t:', file[a+1])
			time.sleep(1)
			print('Password\t\t:', file[a+2])
			time.sleep(1)
			print('Tanggal\t\t\t:', file[a+3])		
		else:
			print('Data tidak ditemukan')
		time.sleep(1)
		menu = input('\nUlangi lagi ? (y/n) ')

	elif menu == 2:
		cari = input('Masukkan nomer brizzi : ')

		if cari in file:
			a = file.index(cari)
			print('Data Tokopedia x Brizzi')
			time.sleep(1)
			print('Nomor Brizzi\t\t:', file[a])
			time.sleep(1)
			print('Nomor HP\t\t: +62', file[a+1])
			time.sleep(1)
			print('Nomor VA\t\t:', file[a+2])
			time.sleep(1)
			print('Password\t\t:', file[a+3])
			time.sleep(1)
			print('Tanggal\t\t\t:', file[a+4])		
		else:
			print('Data tidak ditemukan')
		time.sleep(1)
		menu = input('\nUlangi lagi ? (y/n) ')
	

	if menu == 'y':
		continue
	elif menu == 'n':
		time.sleep(1)
		print('-----------------Terima Kasih ^^----------------')
		time.sleep(1)	
		break
	else:
		print('Input tidak valid')
		break