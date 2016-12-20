import Room


class RoomList():
    def __init__(self):
        self.roomList = {}
    
    def addRoom(self,room):
#        print room.getNamaRoom() + "tersimpan"
        self.roomList[room.getNamaRoom()] = room
        
    def getListRoom(self):
        return self.roomList
    
    def getJumlahRoom(self):
        return len(self.roomList)
    
    def getRoom(self,namaRoom):
        return self.roomList[namaRoom]
