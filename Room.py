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
        self.ranjau_p1_siap = False
        self.ranjau_p2_siap = False
        self.p1_selesai = False
        self.p2_selesai = False
        self.ladang_p1 = []
        self.ladang_p2 = []
        self.tebakan_p1 = []
        self.tebakan_p2 = []
        self.skor_p1 = 0
        self.skor_p2 = 0
        self.skorSudahDihitung = False
        self.p1_gameover = False
        self.p2_gameover = False
        
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
        if self.ranjau_p1_siap is True and self.ranjau_p2_siap is True:
            return True
        else:
            return False

    def cekKesiapanAkhir(self):
        if self.p1_selesai is True and self.p2_selesai is True:
            return True
        else:
            return False

    def cleanLadang(self):
        self.ladang_p1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.ladang_p2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def setLadang(self, player, posisiRanjau):
        if player == 1:
            self.ladang_p1 = posisiRanjau
        else:
            self.ladang_p2 = posisiRanjau

    def getLadang(self, pemain):
        if pemain == 1:
            return self.ladang_p1
        else:
            return self.ladang_p2

    def updateSkor(self):
        if not self.skorSudahDihitung:
            for i in range(4):
                if self.ladang_p1[self.tebakan_p2[i]] == 1:
                    self.skor_p1 += 1
                else:
                    self.skor_p2 += 1

                if self.ladang_p2[self.tebakan_p1[i]] == 1:
                    self.skor_p2 += 1
                else:
                    self.skor_p1 += 1
            self.skorSudahDihitung = True
        else:
            return

    def setUpdateSkorFlag(self, bool):
        self.skorSudahDihitung = bool

    def getSkor(self, pemain):
        if pemain == 1:
            return self.skor_p1
        else:
            return self.skor_p2

    def setTebakan(self, pemain, tebakan):
        if pemain == 1:
            self.tebakan_p1 = tebakan
        else:
            self.tebakan_p2 = tebakan

    def cekGameOver(self):
        if 0 in self.ladang_p1 or 0 in self.ladang_p2:
            return False
        else:
            return True