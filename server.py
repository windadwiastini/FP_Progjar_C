from twisted.internet import reactor
import RoomList
import ServerOpenFactory


room_list = RoomList.RoomList()
print room_list.getListRoom()
factory = ServerOpenFactory.ServerOpenFactory(room_list)
reactor.listenTCP(8124, factory)
reactor.run()
