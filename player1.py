import socket 

MAX_LADANG = 16
sisa ladang = MAX_LADANG
MAX_TEBAK = 4
sudah = [None]*16
sisaladang = 16
tebak = [None]*100
pasang = 0
tebak_buf = [None]*100 
ladang_buf = [None]*100
ladang - [None]*100
pasang = 0
ranjau = 0
skor = [0,0] #[player1, player2]



def pasangranjau():
	i = 1
	while (i <= pasang):
		ranjau = input("Posisi "+i+": ")
		if (ladang[ranjau] != 'X'):
			ladang[ranjau] = 'X'
			sisaladang--
			i++
		else:
			print "Ladang ke-"+ranjau+ "sudah terisi!"

def printscore():
	print "================SCORE================="
	print "Player 1: "+skor[0]+" vs Player 2: "+skor[1]

def tebakin():
	i=1
	while (i <= MAX_TEBAK):
		tebak[i] = input("Tebak lubang lawan: ")
		#socket.send(tebak) -->kirim tebakan kita
		i++

def buatladang():
	i=1
	while (i <= MAX_LADANG):
		ladang[i]='O'
		sudah[i]=0
		i++

def hitungskor():
	i=1
	while(i<= MAX_TEBAK):
		if(sudah[tebak_buf[i]] == 0):
			if(ladang[tebak_buf[i]] == 'X'):
				skor[0]++
			else:
				skor[1]++
		sudah[tebak_buf[i]] = tebak_buf[i]
		i++

def printladang():
	i = j = k = 1
	print "Ladang Ranjau Anda: "
	while (i<=4):
		while(j<=4):
			print ladang[k]
			k++
			j++
		print "\n"
		i++


# socket.send(skor) --> kirim nilai skor
buatladang()
while (sisaladang > 0):
	#system("clear")
	printscore()
	printladang()
	pasang = input("Berapa ingin memasang ranjau (max 4): ")
	while(True):
		if (pasang <= MAX_TEBAK):
			break
		else:
			print "Ulangi masukkan (max 4): "
	print "Pilih lubang yang ingin dipasangi ranjau"
	pasangranjau()
	#socket.send(ladang)
	#system("clear")
	printscore()
	print "Silakan menunggu giliran lawan"
	#tebak_buf = socket.recv(BUFF)
	hitungskor()	
	#socket.send(skor)
	#system("clear")
	printscore()
	print "Silakan menunggu giliran lawan"
	#ladang_buf = socket.recv(BUFF)
	#system("clear")
	printscore()
	tebakin()
	#skor = socket.recv(BUFF)
#system("clear")
printscore()
if (skor[0]>skor[1]):
	print "Pemenangnya adalah Player 1!"
elif (skor[1] > skor[0]):
	print "Pemenangnya adalah Player 2"
else:
	print "Seri!"
#socket.close()


