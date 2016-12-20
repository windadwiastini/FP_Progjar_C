import pygame
import time
# from twisted.internet.protocol import Protocol, ClientFactory
# from twisted.protocols.basic import LineReceiver
# import ClientConnect

class GUI:
    def __init__(self):
        pygame.init()
        self.state = "IDLE"
        self.role = None
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(255,0,0)
        self.lred=(200,0,0)
        self.green=(0,255,0)
        self.lgreen =(0,200,0)
        self.blue=(0,0,255)
        self.lblue=(0,0,200)
        self.blockSize=150
        self.borderSize=15
        self.arrayDataPasang=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.arrayPasang = []
        self.arrayDataPilih=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.arrayPilih=[]
        self.displayWidth = 600
        self.displayHeight = 750
        self.gameDisplay = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        self.smallFont = pygame.font.SysFont(None,32)
        self.medFont = pygame.font.SysFont(None,50)
        self.largeFont = pygame.font.SysFont(None,80)
        self.kotakIsi = self.blockSize-self.borderSize*2
        self.lisNamaRoom = []
        self.namaRoom=""
        pygame.display.set_caption("Benteng Takeshi")
        self.findRoom=False
        self.makeRoom=False
        self.waitingRoom=False
        self.errorRoom=False
        self.intro=False
        self.connectRoom=False
        self.firstRoom=False
        self.loading=False
        self.username=""
        self.turn = True
        self.score1 = 0
        self.score2 = 0
        self.jumlahPasangTebak=0
        self.i=0

        # self.client = client

    # def jalankan(self):
    #     while True:
    #         if self.client.getStatusMessage() is False:
    #             print self.client.getIncomingMsg()
    #             self.first_room()
    #             break

    def arenaPasang(self):
        index=0
        for i in range(4):
            tileSizeI = i * self.blockSize
            for j in range(4):
                tileSizeJ = j * self.blockSize
                if self.arrayDataPasang[index]==1:
                    pygame.draw.rect(self.gameDisplay, self.black,[tileSizeI + self.borderSize, tileSizeJ + self.borderSize, self.kotakIsi, self.kotakIsi])
                else:
                    pygame.draw.rect(self.gameDisplay, self.red, [tileSizeI, tileSizeJ, self.blockSize, self.blockSize],self.borderSize)
                temp = (tileSizeI, tileSizeJ)
                self.arrayPasang.append(temp)
                # print self.arrayPasang
                index+=1

    def arenaPilih(self):
        index=0
        for i in range(4):
            tileSizeI = i * self.blockSize
            for j in range(4):
                tileSizeJ = j * self.blockSize
                if self.arrayDataPasang[index] == 1:
                    pygame.draw.rect(self.gameDisplay, self.black,[tileSizeI + self.borderSize, tileSizeJ + self.borderSize, self.kotakIsi,self.kotakIsi])
                else:
                    pygame.draw.rect(self.gameDisplay, self.red, [tileSizeI, tileSizeJ, self.blockSize, self.blockSize], self.borderSize)
                temp = (tileSizeI, tileSizeJ)
                self.arrayPilih.append(temp)
                index+=1
    def button(self,x,y,key):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+self.blockSize > cur[0] > x and y+self.blockSize > cur[1] > y:
            # pygame.draw.rect(self.gameDisplay,self.black,(x+self.borderSize,y+self.borderSize,self.kotakIsi,self.kotakIsi))
            if click[0] == 1:
                self.clicked(x, y, key)
                print


        # else :
        #     if self.turn:
        #         self.turn=False
        #     else:
        #         self.turn=True

    def clicked(self,x,y,key):
        if self.arrayDataPasang[key]==0:
            if self.turn:
                self.arrayDataPilih = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.arrayDataPasang[key]=1
                print self.arrayDataPasang
                # pygame.draw.rect(self.gameDisplay, self.black,(x + self.borderSize, y + self.borderSize, self.kotakIsi, self.kotakIsi))
                self.jumlahPasangTebak += 1
            else :
                self.arrayDataPilih[key]=1
                # pygame.draw.rect(self.gameDisplay, self.black,(x + self.borderSize, y + self.borderSize, self.kotakIsi, self.kotakIsi))
        else :
            pass



    def insertText(self,text,color,size):
        if size=="small":
            textSurface = self.smallFont.render(text, True, color)
        if size == "med":
            textSurface = self.medFont.render(text, True, color)
        if size == "large":
            textSurface = self.largeFont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def showText(self,isi,color,posisiY,size="small"):
        textSurf,textRect = self.insertText(isi,color,size)
        textRect.center = (self.displayWidth/2),(posisiY)
        self.gameDisplay.blit(textSurf,textRect)

    def showScore(self,isi,color,posisiX,size="small"):
        textSurf , textRect = self.insertText(isi,color,size)
        textRect.center = (posisiX),650
        self.gameDisplay.blit(textSurf,textRect)

    def scoreBoard(self):
        pygame.draw.rect(self.gameDisplay, self.black, [0, 600, 600, 150])
        pygame.display.update()

    def insertTextButton(self,text,color,x,y,width,height,size="small"):
        textSurf,textRect = self.insertText(text,color,size)
        textRect.center = ((x+width/2),(y+height/2))
        self.gameDisplay.blit(textSurf,textRect)

    def menuPanel(self,text,y,colorActive,colorinActive,x,action=None,param=""):
        cur = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        menuWidth = 200
        menuHeight = 50

        if x+menuWidth > cur[0] > x and y+menuHeight > cur[1] > y:
            pygame.draw.rect(self.gameDisplay,colorActive,(x,y,menuWidth,menuHeight))
            if clicked[0]==1:
                if action=="quit":
                    pygame.quit()
                    quit()
                elif action=="makeRoom":
                    pesan = self.make_room()
                    self.intro=False
                    return pesan
                elif action =="joinRoom":
                    self.intro=False
                    return "LISTR"
                elif action=="waitingRoom":
                    self.makeRoom = False
                elif action=="readyToPlay":
                    self.findRoom = False
                    return "JOINR "+param
                elif action=="intro":
                    self.firstRoom=False

        else :
            pygame.draw.rect(self.gameDisplay, colorinActive, (x, y, menuWidth, menuHeight))
        self.insertTextButton(text,self.black,x,y,menuWidth,menuHeight)


    def game_intro(self):
        self.intro = True
        creater = None
        listr = None
        keluar = None
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.white)
            self.showText("Selamat Datang "+self.username+" !",self.red,300,"med")
            creater = self.menuPanel("Bikin Room",400,self.lblue,self.blue,self.displayWidth/2-100,action="makeRoom")
            listr = self.menuPanel("Join Room", 500,self.lgreen,self.green,self.displayWidth/2-100,action="joinRoom")
            keluar = self.menuPanel("Quit", 600, self.lred,self.red,self.displayWidth / 2 - 100,action="quit")
            pygame.display.update()
        if creater is not None:
            return creater
        elif listr is not None:
            return listr
        elif keluar is not None:
            return keluar

    def find_room(self,arrayRoom):
        self.findRoom = True
        room =[]
        while self.findRoom:
            x=200
            self.gameDisplay.fill(self.white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.showText("List Room",self.red,100,"large")
            for namaRoom in arrayRoom:
                x+=100
                room.append(self.menuPanel(namaRoom, x, self.lgreen, self.green, self.displayWidth / 2 - 100, action="readyToPlay",param=namaRoom))
            for name in room:
                if name is not None:
                    return name
            pygame.display.update()


    def make_room(self):
        self.makeRoom = True
        while self.makeRoom:
            self.gameDisplay.fill(self.white)
            self.showText("Ketik Nama Room",self.black,300,"large")
            self.showText(self.namaRoom,self.black,self.displayHeight/2,"med")
            self.menuPanel("Bikin Room!", 650, self.lblue, self.blue, self.displayWidth/2-100, action="waitingRoom")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if pygame.K_a <= event.key <= pygame.K_z or pygame.K_0 < event.key < pygame.K_9 or event.key==pygame.K_SPACE:
                        character = chr(event.key)
                        self.namaRoom+=str(character)
                    elif pygame.K_BACKSPACE == event.key:
                        self.namaRoom = self.namaRoom[:-1]
        return "CREATER "+self.namaRoom

    def first_room(self):
        self.firstRoom = True
        while self.firstRoom:
            self.gameDisplay.fill(self.white)
            self.showText("Benteng Takeshi", self.red, 300, "large")
            self.showText("Masukan Username Kamu",self.black,400,"med")
            self.showText(self.username,self.black,450)
            self.menuPanel("Submit!",650, self.lblue, self.blue, self.displayWidth/2-100, action="intro")
            pygame.display.update()
            # print "masih masuk"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if pygame.K_a <= event.key <= pygame.K_z or pygame.K_0 < event.key < pygame.K_9 or event.key==pygame.K_SPACE:
                        character = chr(event.key)
                        self.username+=str(character)
                    elif pygame.K_BACKSPACE == event.key:
                        self.username = self.username[:-1]
        return self.username


    def waiting_room(self):
        self.waitingRoom = True
        while self.waitingRoom:
            self.gameDisplay.fill(self.white)
            self.showText("Menunggu Lawan . . .",self.black,self.displayHeight/2,"large")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            break

    def error_nama_room(self):
        self.errorRoom = True
        while self.errorRoom:
            self.gameDisplay.fill(self.white)
            self.showText("Nama Room Sudah Terdaftar!",self.black,self.displayHeight/2,"large")
            self.menuPanel("Back", 500, self.lred, self.red, self.displayWidth / 2 - 100, action="makeRoom")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def connect_room(self):
        self.connectRoom=True
        while self.connectRoom:
            self.gameDisplay.fill(self.white)
            self.showText("Loading . . .", self.black, self.displayHeight / 2, "large")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            time.sleep(5)
            self.connectRoom=False
        return

    def loadingScreen(self):
        self.loading=True
        while self.loading:
            self.gameDisplay.fill(self.white)
            self.showText("Loading . . .", self.black, self.displayHeight / 2, "large")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.loading=False

    def inGameWaitingScreen(self):
        self.loading = True
        while self.loading:
            self.gameDisplay.fill(self.white)
            self.showText("Menunggu Lawan Selesai . . .", self.black, self.displayHeight / 2, "large")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.loading = False

    def gameLoop(self,skor1,skor2,ladang,myTurn):
        self.score1=skor1
        self.score2=skor2
        self.arrayPasangData = ladang
        self.turn = myTurn
        gameExit = False
        gameOver = False
        self.gameDisplay.fill(self.white)
        self.scoreBoard()
        self.jumlahPasangTebak=0
        pygame.display.update()


        while not gameExit:

            self.showScore("Score: " + str(self.score1), self.lgreen, 150)
            self.showScore("Score: " + str(self.score2), self.lred, 450)

            while gameOver==True:
                self.youWin()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            if self.turn:
                self.arenaPasang()
                self.showText("Memasang Ranjau",self.red,675)
                if self.jumlahPasangTebak>=4:
                    return self.arrayDataPasang

            else :
                self.arenaPilih()
                self.showText("Memilih Lubang",self.green,675)
                if self.jumlahPasangTebak>=4:
                    return self.arrayDataPilih


            koor_x = [seq[0] for seq in self.arrayPasang]
            koor_y = [seq[1] for seq in self.arrayPasang]

            self.button(koor_x[0], koor_y[0], 0)
            self.button(koor_x[1], koor_y[1], 1)
            self.button(koor_x[2], koor_y[2], 2)
            self.button(koor_x[3], koor_y[3], 3)
            self.button(koor_x[4], koor_y[4], 4)
            self.button(koor_x[5], koor_y[5], 5)
            self.button(koor_x[6], koor_y[6], 6)
            self.button(koor_x[7], koor_y[7], 7)
            self.button(koor_x[8], koor_y[8], 8)
            self.button(koor_x[9], koor_y[9], 9)
            self.button(koor_x[10], koor_y[10], 10)
            self.button(koor_x[11], koor_y[11], 11)
            self.button(koor_x[12], koor_y[12], 12)
            self.button(koor_x[13], koor_y[13], 13)
            self.button(koor_x[14], koor_y[14], 14)
            self.button(koor_x[15], koor_y[15], 15)

            pygame.display.update()
        pygame.quit()
        quit()


    def youLose(self):
        self.gameDisplay.fill(self.red)
        self.showText("YOU LOSE",self.black,self.displayHeight/2,"large")


    def youWin(self):
        self.gameDisplay.fill(self.green)
        self.showText("YOU WIN",self.black,self.displayHeight/2,"large")


ingame = GUI()
ingame.gameLoop(1,2,3,True)