import Gameplay

class Room():
    def __init__(self, users,nama):
        self.roomMaster = users
        self.nama = nama
        self.penantang = None
        self.ready = False
        self.game = None
        self.ranjau_p1_siap = False
        self.ranjau_p2_siap = False
        self.p1_selesai = False
        self.p2_selesai = False
        
    def getNamaRoom(self):
        return self.nama
    
    def getStatus(self):
        return self.ready
    
    def addPenantang(self,penantang):
        self.penantang = penantang
        self.ready = True
    
    def getPenantang(self):
        return self.penantang

    def getRoomMaster(self):
        return self.roomMaster

    def startGame(self):
        self.game = Gameplay.Gameplay()
        return self.game

    def set_ranjau_siap(self, pemain, bool):
        if pemain == 1:
            self.ranjau_p1_siap = bool
        else:
            self.ranjau_p2_siap = bool

    def set_kesiapan_akhir(self, pemain, bool):
        if pemain == 1:
            self.p1_selesai = bool
        else:
            self.p2_selesai = bool

    def cekKesiapanRanjau(self):
        if self.ranjau_p1_siap == True and self.ranjau_p2_siap == True:
            return True
        else:
            return False

    def cekKesiapanAkhir(self):
        if self.p1_selesai == True and self.p1_selesai == True:
            return True
        else:
            return False