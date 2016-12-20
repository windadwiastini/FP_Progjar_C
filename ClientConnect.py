import json
from twisted.protocols.basic import LineReceiver
import time
import GUI


class ClientConnect(LineReceiver):
    def lineReceived(self, line):
        pass

    def rawDataReceived(self, data):
        pass

    def __init__(self):
        self.incomingMsg = ""
        self.state = "IDLE"
        self.role = None
        self.pesanSudahDibaca = True
        self.view = GUI.GUI()

    def play(self, state, skor_p1, skor_p2, ladang):
        if state == "PASANG":
            ladangku = self.view.gameLoop(skor_p1, skor_p2, ladang, True)
            paket_ladangku = json.dumps(ladangku)
            self.sendLine("RANJAUKU // "+paket_ladangku)
            self.view.loadingScreen()
        elif state == "TEBAK":
            tebakan = self.view.gameLoop(skor_p1, skor_p2, ladang, False)
            print "tebakan: ", tebakan
            paket_tebakan = json.dumps(tebakan)
            # print paket_tebakan
            self.sendLine("TEBAKANKU // "+paket_tebakan)
            self.view.loadingScreen()

    def waiting(self):
        self.state = "WAITING"
        print "Menunggu penantang untuk bergabung..."
        time.sleep(1)
        self.sendLine("CEK_PENANTANG")
        self.view.waiting_room()

    # def play(self, data):
    #     if self.state == "READ":
    #         print data
    #     else:
    #         print data
    #         msg = raw_input()
    #         self.sendLine(msg)

    def tungguLawan(self, pesan):
        time.sleep(1)
        msg = self.sendLine(pesan)
        print msg

    def dataReceived(self, data):
        print "Server: ", data
        if data == "ROOM_CREATED\r\n" or data == "WAITING\r\n":
            self.waiting()
        elif data == "USERNAME\r\n":
            messageClient = self.view.first_room()
            self.sendLine(messageClient)
            self.view.loadingScreen()
        elif data == "WELCOME\r\n":
            messageClient = self.view.game_intro()
            print "client: ", messageClient
            self.kirimPesan(str(messageClient))
            self.view.loadingScreen()
        elif "LOAD_LIST" in data:
            paket = data.split('LOAD_LIST ')[1]
            paketList = json.loads(paket)
            # print len(paketList)
            # for i in paketList:
            #     print i
            messageClient = self.view.find_room(paketList)
            # print "Client: ", messageClient
            self.kirimPesan(messageClient)
            self.view.loadingScreen()
        elif data == "GAME_START\r\n":
            # print "[Mode read]\n"
            self.view.connect_room()
            self.state = "PLAY"
            self.sendLine("IM_READY")
            # self.view.connect_room()
        elif "GAME_OVER" in data:
            skor = data.split(' // ')[0]
            skor_p1 = skor.split(' vs ')[0]
            skor_p2 = skor.split(' vs ')[1]
            if self.role=="RAJA":
                if skor_p1 >= skor_p2:
                    self.view.youWin()
                else:
                    self.view.youLose()
            else:
                if skor_p2 >= skor_p1:
                    self.view.youWin()
                else:
                    self.view.youLose()
        else:
            if self.state == "PLAY":
                if "RANJAU_TERPASANG" in data or "MUSUH_BELUM_SIAP" in data:
                    self.tungguLawan("APAKAH_PLAYER_LAIN_SIAP")
                elif "TEBAKAN_DITAMPUNG" in data or "MUSUH_BELUM_SELESAI" in data:
                    self.tungguLawan("APAKAH_PLAYER_LAIN_SELESAI")
                else:
                    print data
                    skor = data.split(' // ')[0]
                    state = data.split(' // ')[1]
                    paket_ladang = data.split(' // ')[2]
                    skor_p1 = skor.split(' vs ')[0]
                    skor_p2 = skor.split(' vs ')[1]
                    ladang = json.loads(paket_ladang)
                    self.play(state, skor_p1, skor_p2, ladang)

    def kirimPesan(self, pesan):
        self.sendLine(pesan.encode("utf8"))
