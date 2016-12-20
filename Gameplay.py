class Gameplay:
    def __init__(self):
        self.ladang_p1 = []
        self.ladang_p2 = []
        self.tebakan_p1 = []
        self.tebakan_p2 = []
        self.skor_p1 = 0
        self.skor_p2 = 0


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
        for i in range(4):
            if self.ladang_p1[self.tebakan_p2[i]] == 1:
                self.skor_p1 += 1
            else:
                self.skor_p2 += 1

            if self.ladang_p2[self.tebakan_p1[i]] == 1:
                self.skor_p2 += 1
            else:
                self.skor_p1 += 1

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