from twisted.internet.protocol import Factory
import RoomList
import ServerOpen


class ServerOpenFactory(Factory):
    def __init__(self,room_list):
        self.users = {} # maps user names to Chat instances
        self.room_list = room_list

    def buildProtocol(self, addr):
        print self.users
        return ServerOpen.ServerOpen(self.users,self.room_list)