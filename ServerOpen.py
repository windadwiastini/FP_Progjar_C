from twisted.protocols.basic import LineReceiver
import Room
import json

class ServerOpen(LineReceiver):
    def __init__(self, users, room_list):
        self.users = users
        self.name = None
        self.state = "GETNAME"
        self.room_list= room_list
        self.newRoom = None
        self.threads = []
        self.lawan = None
        self.role = None
        self.game = None

    def connectionMade(self):
        print "Client masuk"
        self.sendLine("USERNAME")

    def connectionLost(self, reason):
        if self.users.has_key(self.name):
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            nama = "Client"
        else:
            nama = self.name
        print nama+": "+line
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        elif self.state == "MAIN_MENU":
            self.handle_MAIN_MENU(line)
        elif self.state == "WAITING" or line == "CEK_PENANTANG":
            self.handle_WAITING()
        elif self.state == "PLAY":
            self.handle_PLAY(line)
        else:
            self.sendLine("Perintah tidak diketahui\n")
    
    def main_menu(self):
        # message = "Username: "+self.name+"\n\nMAIN MENU\n>>Lihat Daftar Room: LISTR\n>>Buat Room Baru: CREATER nama_room(tanpa spasi)\n>>Join room: JOINR nama_room"
        self.state = "MAIN_MENU"
        # return message
    
    def handle_WAITING(self):
        if self.newRoom.getStatus() is True:
            self.state = "PLAY"
            self.role == "RAJA"
            self.lawan = self.newRoom.getPenantang()
            self.game = self.newRoom.startGame()
            self.sendLine("GAME_START")
        else:
            self.sendLine("WAITING")
            
    
    def handle_GETNAME(self, name):
        if self.users.has_key(name):
            self.sendLine("Username sudah digunakan, silakan pakai nama lain")
            return
        self.sendLine("WELCOME")
        self.name = name
        self.users[name] = self
        print self.name," telah bergabung!"
        self.main_menu()
        # self.sendLine(self.main_menu())

    def handle_MAIN_MENU(self, message):
        command = message.split(' ')[0]
        if command == "CREATER":
            content = message.split(' ')[1]
            if content in self.room_list.getListRoom():
                pesan = "Nama room sudah digunakan, gunakan nama lain yang unik" + self.main_menu()
                self.sendLine(pesan)
            else:
                self.newRoom = Room.Room(self, content)
                self.room_list.addRoom(self.newRoom)
                print self.name+" telah membuat room dengan nama "+self.newRoom.getNamaRoom()
                self.state = "WAITING"
                self.role = "RAJA"
                self.sendLine("ROOM_CREATED")
        elif command == "LISTR":
            pesan = []
            for key, value in self.room_list.getListRoom().iteritems():
                pesan.append(key)
            self.main_menu()
            paket = json.dumps(pesan)
            self.sendLine("LOAD_LIST "+paket)
        elif command == "JOINR":
            pesan = ""
            content = message.split(' ')[1]
            if content in self.room_list.getListRoom():
                self.newRoom = self.room_list.getRoom(content)
                self.newRoom.addPenantang(self)
                self.lawan = self.newRoom.getRoomMaster()
                self.state = "PLAY"
                self.role = "PENANTANG"
                self.game = self.newRoom.startGame()
                self.sendLine("GAME_START")
            else:
                pesan = "\nTidak ada room dengan nama "+content+"\n"+self.main_menu()
                self.sendLine(pesan)

    def pasangRanjau(self):
        if self.role == "RAJA":
            ladang = self.game.getLadang(1)
            paket_ladang = json.dumps(ladang)
        else:
            ladang = self.game.getLadang(2)
            paket_ladang = json.dumps(ladang)
        return "PASANG // "+paket_ladang

    def tebakRanjau(self):
        if self.role == "RAJA":
            ladang = self.game.getLadang(2)
            paket_ladang = json.dumps(ladang)
        else:
            ladang = self.game.getLadang(1)
            paket_ladang = json.dumps(ladang)
        return "TEBAK // " + paket_ladang

    def handle_PLAY(self, line):
        pesan = str(self.game.getSkor(1))+" vs "+str(self.game.getSkor(1))+" // "
        if "IM_READY" in line:
            self.game.cleanLadang()
            pesan = pesan+self.pasangRanjau()
            print pesan
        elif "APAKAH_PLAYER_LAIN_SIAP" in line:
            if self.newRoom.cekKesiapanRanjau() is False:
                self.sendLine("MUSUH_BELUM_SIAP")
                return
            else:
                pesan = pesan+self.tebakRanjau()
        elif "APAKAH_PLAYER_LAIN_SELESAI" in line:
            if self.newRoom.cekKesiapanAkhir() == False:
                self.sendLine("MUSUH_BELUM_SELESAI")
            else:
                self.game.updateSkor()
                pesan = str(self.game.getSkor(1)) + " vs " + str(self.game.getSkor(1)) + " // "
                pesan = pesan + self.pasangRanjau()
        elif "RANJAUKU" in line:
            ladang = line.split(" // ")[1]
            if self.role == "RAJA":
                self.game.setLadang(1, ladang)
                self.game.set_ranjau_siap(1, True)
                self.game.set_kesiapan_akhir(1, False)
            else:
                self.game.setLadang(2, ladang)
                self.game.set_ranjau_siap(2, True)
                self.game.set_kesiapan_akhir(2, False)
            self.sendLine("RANJAU_TERPASANG")
            return
        elif "TEBAKANKU" in line:
            tebakan = line.split(" // ")[1]
            if self.role == "RAJA":
                self.game.setTebakan(1, tebakan)
                self.game.set_kesiapan_akhir(1, True)
                self.game.set_ranjau_siap(1, False)
            else:
                self.game.setTebakan(2, tebakan)
                self.game.set_kesiapan_akhir(2, True)
                self.game.set_ranjau_siap(2, False)
            self.sendLine("TEBAKAN_DITAMPUNG")
            return
        self.sendLine(pesan)